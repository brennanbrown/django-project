# AWS S3 Setup for Media Files

This guide explains how to configure AWS S3 to store media files (uploaded images) for your Django project on Heroku.

## Why Use S3?

Heroku's filesystem is **ephemeral** - any files uploaded to your app (images, documents, etc.) will be deleted when:
- The dyno restarts (at least once per day)
- You deploy new code
- Heroku performs maintenance

**Solution**: Store media files in Amazon S3 (Simple Storage Service) for permanent storage.

---

## Prerequisites

- AWS account (free tier available)
- Django project deployed on Heroku
- Credit card for AWS (required even for free tier, but S3 is very cheap: ~$0.023/GB/month)

---

## Step 1: Create S3 Bucket

### 1. Go to AWS S3 Console
Visit: https://console.aws.amazon.com/s3/

### 2. Create Bucket
1. Click **"Create bucket"**
2. **Bucket name**: Choose a unique name (e.g., `your-app-name-media`)
   - Must be globally unique across all AWS
   - Use lowercase, numbers, and hyphens only
3. **Region**: Select closest to your users (e.g., `us-east-1` for US East Coast)
4. **Block Public Access settings**:
   - ⚠️ **Uncheck** "Block all public access"
   - Check the acknowledgment box
   - (This allows public read access to your images)
5. **Bucket Versioning**: Disabled (unless you need it)
6. Click **"Create bucket"**

### 3. Configure Bucket Policy (Optional but Recommended)

1. Click on your newly created bucket
2. Go to **"Permissions"** tab
3. Scroll to **"Bucket policy"** → Click **"Edit"**
4. Paste this policy (replace `YOUR-BUCKET-NAME`):

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::YOUR-BUCKET-NAME/*"
        }
    ]
}
```

5. Click **"Save changes"**

### 4. Configure CORS (if needed for uploads)

1. Still in **"Permissions"** tab
2. Scroll to **"Cross-origin resource sharing (CORS)"**
3. Click **"Edit"** and paste:

```json
[
    {
        "AllowedHeaders": ["*"],
        "AllowedMethods": ["GET", "PUT", "POST", "DELETE"],
        "AllowedOrigins": ["*"],
        "ExposeHeaders": []
    }
]
```

4. Click **"Save changes"**

---

## Step 2: Create IAM User

### 1. Go to IAM Console
Visit: https://console.aws.amazon.com/iam/

### 2. Create User
1. Click **"Users"** (left sidebar) → **"Add users"**
2. **User name**: `django-s3-user` (or similar)
3. Click **"Next"**

### 3. Set Permissions
1. Select **"Attach policies directly"**
2. Search for: `AmazonS3FullAccess`
3. Check the box next to **AmazonS3FullAccess**
4. Click **"Next"** → **"Create user"**

### 4. Create Access Keys
1. Click on the user you just created
2. Go to **"Security credentials"** tab
3. Scroll to **"Access keys"** → Click **"Create access key"**
4. Select **"Application running outside AWS"**
5. Click **"Next"** → **"Create access key"**
6. **🔴 IMPORTANT**: Copy both:
   - **Access key ID** (starts with `AKIA...`)
   - **Secret access key** (long random string)
   - You won't be able to see the secret key again!
7. Click **"Done"**

---

## Step 3: Configure Django Project

Your Django project is already configured for S3! The settings are in `portfolio/settings.py`:

```python
# AWS S3 Settings for Media Files
USE_S3 = os.environ.get('USE_S3', 'False') == 'True'

if USE_S3:
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_REGION_NAME = os.environ.get('AWS_S3_REGION_NAME', 'us-east-1')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    AWS_DEFAULT_ACL = 'public-read'
    
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'
```

**Dependencies already installed**:
- `boto3` - AWS SDK for Python
- `django-storages` - Django storage backends

---

## Step 4: Add Config Vars to Heroku

### 1. Go to Heroku Dashboard
Visit: https://dashboard.heroku.com/apps/YOUR-APP-NAME/settings

### 2. Reveal Config Vars
Click **"Reveal Config Vars"**

### 3. Add These Variables

| Key | Value | Example |
|-----|-------|---------|
| `USE_S3` | `True` | `True` |
| `AWS_ACCESS_KEY_ID` | Your access key | `AKIAIOSFODNN7EXAMPLE` |
| `AWS_SECRET_ACCESS_KEY` | Your secret key | `wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY` |
| `AWS_STORAGE_BUCKET_NAME` | Your bucket name | `my-django-app-media` |
| `AWS_S3_REGION_NAME` | Your AWS region | `us-east-1` |

⚠️ **Security Note**: Never commit these keys to Git! They should only be in Heroku Config Vars.

### 4. Restart Your App (Optional)
Heroku usually restarts automatically when you change config vars. If not:
- Click **"More"** → **"Restart all dynos"**

---

## Step 5: Test It Out

### 1. Upload an Image
1. Go to your admin panel: `https://your-app.herokuapp.com/admin/`
2. Add a new Job with an image
3. Click **"Save"**

### 2. Verify S3 Storage
1. Go back to your S3 bucket in AWS Console
2. You should see a `media/` folder with your uploaded image
3. The image URL will be: `https://your-bucket-name.s3.amazonaws.com/media/images/filename.jpg`

### 3. Check Your Website
Visit your site - the image should display correctly!

---

## Troubleshooting

### Images not uploading

**Check Heroku logs**:
```bash
heroku logs --tail --app your-app-name
```

**Common issues**:
- ❌ Wrong AWS credentials → Check Config Vars match IAM user keys
- ❌ Bucket doesn't exist → Check bucket name spelling
- ❌ Wrong region → Check `AWS_S3_REGION_NAME` matches bucket region
- ❌ Permission denied → Check IAM user has S3 access

### Images upload but don't display

**Check bucket policy**:
- Ensure "Block all public access" is OFF
- Verify bucket policy allows public `GetObject`

**Check CORS configuration**:
- Add CORS policy if uploading from browser

### Want to verify S3 is working?

Check your Heroku logs after uploading:
```
heroku logs --tail --app your-app-name
```

You should NOT see local filesystem paths like `/app/media/...`. Instead, you should see S3 URLs.

---

## Cost Estimates

AWS S3 Free Tier (first 12 months):
- **5 GB** of standard storage
- **20,000** GET requests
- **2,000** PUT requests

After free tier (approximate):
- **Storage**: $0.023 per GB/month
- **Requests**: $0.0004 per 1,000 GET requests
- **Data transfer**: First 1 GB free, then $0.09 per GB

**Example cost for a small portfolio**:
- 100 MB of images = $0.002/month
- 1,000 page views = $0.001/month
- **Total: Less than $0.01/month** 💰

---

## Alternative: Cloudinary

If you prefer a simpler solution, consider [Cloudinary](https://cloudinary.com/):
- ✅ Easier setup (no IAM users)
- ✅ Free tier: 25 GB storage, 25 GB bandwidth
- ✅ Built-in image transformations
- ❌ Less control than S3
- ❌ Vendor lock-in

---

## Security Best Practices

### 1. Use IAM User (Not Root Account)
✅ Create dedicated IAM user for Django
❌ Don't use root AWS credentials

### 2. Limit Permissions
✅ Use `AmazonS3FullAccess` or create custom policy for specific bucket
❌ Don't use `AdministratorAccess`

### 3. Rotate Keys Regularly
- Generate new access keys every 6-12 months
- Delete old keys after rotation

### 4. Never Commit Keys to Git
✅ Use Heroku Config Vars or `.env` files (in `.gitignore`)
❌ Don't hardcode in `settings.py`

### 5. Use Environment-Based Configuration
Already implemented in your `settings.py`:
```python
USE_S3 = os.environ.get('USE_S3', 'False') == 'True'
```

This allows:
- Local development without S3
- Production with S3
- Easy switching between environments

---

## Local Development

Your project is configured to use local filesystem in development:

```python
# When USE_S3=False (default for local dev)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

**For local testing with S3**:
Add to your `.env` file:
```
USE_S3=True
AWS_ACCESS_KEY_ID=your-key
AWS_SECRET_ACCESS_KEY=your-secret
AWS_STORAGE_BUCKET_NAME=your-bucket
AWS_S3_REGION_NAME=us-east-1
```

---

## Advanced Configuration

### Custom Storage Classes

If you want separate buckets for static and media files:

```python
# Custom storage backends
from storages.backends.s3boto3 import S3Boto3Storage

class MediaStorage(S3Boto3Storage):
    location = 'media'
    file_overwrite = False

# In settings.py
DEFAULT_FILE_STORAGE = 'yourapp.storage_backends.MediaStorage'
```

### CloudFront CDN

For faster global delivery, add CloudFront in front of S3:
1. Create CloudFront distribution
2. Point origin to S3 bucket
3. Update `AWS_S3_CUSTOM_DOMAIN` to CloudFront URL

---

## Resources

- **AWS S3 Documentation**: https://docs.aws.amazon.com/s3/
- **django-storages Documentation**: https://django-storages.readthedocs.io/
- **boto3 Documentation**: https://boto3.amazonaws.com/v1/documentation/api/latest/index.html
- **Heroku + S3 Guide**: https://devcenter.heroku.com/articles/s3

---

## Summary

✅ **What We Set Up**:
1. S3 bucket for storing media files
2. IAM user with S3 access
3. Django configured to use S3 in production
4. Heroku Config Vars for AWS credentials

✅ **Benefits**:
- Permanent media file storage
- Scalable (handles any number of files)
- Fast delivery (from AWS edge locations)
- Very low cost
- Production-ready

🎉 Your Django app now has persistent media storage!

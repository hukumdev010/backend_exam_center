# Deployment Setup Instructions

## Setting up Private Repository Access for EC2 Deployment

The updated deployment workflow now pulls code directly from the private GitHub repository on the EC2 instance. To make this work, you need to set up authentication.

### Option 1: Deploy Key (Recommended)

1. **Generate a new SSH key pair on your local machine:**
   ```bash
   ssh-keygen -t ed25519 -C "github-deploy-key" -f ~/.ssh/github_deploy_key
   ```

2. **Add the public key as a Deploy Key to your GitHub repository:**
   - Go to your repository: https://github.com/hukumdev010/backend_exam_center
   - Navigate to Settings → Deploy keys
   - Click "Add deploy key"
   - Title: "EC2 Deployment Key"
   - Key: Copy the contents of `~/.ssh/github_deploy_key.pub`
   - Check "Allow write access" if you need to push from EC2 (optional)
   - Click "Add key"

3. **Add the private key to GitHub Actions secrets:**
   - Go to your repository Settings → Secrets and variables → Actions
   - Click "New repository secret"
   - Name: `GITHUB_DEPLOY_KEY`
   - Value: Copy the contents of `~/.ssh/github_deploy_key` (the private key)
   - Click "Add secret"

### Option 2: Personal Access Token (Alternative)

If you prefer using a token instead of SSH keys:

1. **Generate a Personal Access Token:**
   - Go to GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
   - Generate a new token with `repo` scope
   - Copy the token

2. **Add token to GitHub Actions secrets:**
   - Repository Settings → Secrets and variables → Actions
   - Name: `GITHUB_TOKEN`
   - Value: Your personal access token

3. **Update the deployment script to use HTTPS instead of SSH:**
   - Change the git clone URL from `git@github.com:hukumdev010/backend_exam_center.git` 
   - To: `https://$GITHUB_TOKEN@github.com/hukumdev010/backend_exam_center.git`

### Required GitHub Secrets

Make sure these secrets are set in your repository:

- `EC2_HOST`: Your EC2 instance IP address (currently: 13.219.66.17)
- `EC2_USER`: EC2 username (ubuntu)
- `EC2_SSH_PRIVATE_KEY`: SSH private key for EC2 access
- `GITHUB_DEPLOY_KEY`: SSH private key for GitHub repository access (if using Option 1)

### Testing the Deployment

1. Push changes to the master branch
2. Check the Actions tab in your GitHub repository
3. Monitor the deployment workflow execution
4. Verify the application is running at http://your-ec2-ip:8000/docs

### Troubleshooting

- **SSH Permission Denied**: Check that the deploy key is correctly added to GitHub and the secret is properly set
- **Repository Not Found**: Ensure the deploy key has the correct permissions and the repository URL is correct
- **Service Start Issues**: Check systemd logs with `sudo journalctl -u exam-center-backend -f`
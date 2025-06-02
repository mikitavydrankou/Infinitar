# How to setup MLFlow on DigitalOcean (STEP BY STEP)

> [MLFlow quickstart (youtube)](https://www.youtube.com/watch?v=cjeCAoW83_U)
> 
> [MLFLow setup script (github)](https://github.com/mikitavydrankou/MLflow-server-ubuntu24)
>
> DigitalOcean gives 200$ for students, look more in [Github Student pack](https://education.github.com/pack)

1. ## DigitalOcean configuration

    1. Setup SSH keys on DigitalOcean
        1. Go to settings and find Security tab
        2. Go to “Add SSH Key”
        3. Follow instructions on right side (save your passphrase somewhere, we need it later)
        4. Done with SSH keys!
    2. Create Project
        1. Click on “New Project” at the left bar
        2. Enter name and choose purpose (choose one you want, not depends, but i prefer AI, its all about recommendations)
    3. Configuring Droplet (skip options, if they are not mentioned)
        1. Click on green “Create” button on top and choose “Droplets”
        2. Choose closest region to you
        3. By default, there is Ubuntu 24.10 x64, if not, choose it
        4. For MLFlow we can choose Basic plan, with Regular config (Disk type: SSD) for $12
        5. Choose SSH key, you have created
        6. Give hostname for Droplet
        7. Choose your project and create droplet
    4. Configuring S3
        1. Click on “Create” (where we chose Droplets), and click on “Spaces Object Storage”
        2. Click “Enable CDN”
        3. Give unique Bucket name
        4. Choose your project
        5. Create your Space Bucket (S3 storage)

2. ## Connecting to Droplet

    1. Go to your project and click on IP (E.g 67.182.42.230), it will copy IP to buffer
    2. Go to your terminal (on Windows - PowerShell), type ssh root@, paste ip after @ (E.g. `ssh root@67.182.42.230`), and click Enter
    3. First time, It will ask “Are you sure you want to continue…”, type “yes”
    4. Next, It will ask for passphrase, type it and push enter, it will be asked every time you trying to connect. At this moment you should be successfully connected to your Droplet

3. ## Configuring MLFlow Server

    1. Go to https://github.com/mikitavydrankou/MLflow-server-ubuntu24 and copy link to project
    2. Git clone this script (`git clone https://github.com/mikitavydrankou/MLflow-server-ubuntu24.git`)
    3. Go to script directory → `cd MLflow-server-ubuntu24`
    4. Copy template of env file → `cp .env.example .env`
    5. Edit .env → `nano .env`
        1. You can leave variables that starts from PG\_…
        2.` MLFLOW_BUCKET_NAME=`
            1. Pass your unique name of bucket
        2. `AWS_ACCESS_KEY_ID=`
            1. Go to DigitalOcean, find bucket you have created earlier and click on it
            2. Go to settings, scroll down and find “Access Keys”
            3. Click on “Create Access Key”
            4. Select “Limited Access” at “Select access scope”
            5. Choose your bucket and change Permissions to “Read/Write/Delete”
            6. You can skip or give a name to your key
            7. Click on “Create Access Key”
            8. Now you will see “Access key ID” column. Copy this and pass to variable in .env (Don’t reload page! Copy secret key!)
        3. `AWS_SECRET_ACCESS_KEY=`
            1. Paste your secret key to .env
        4. `MLFLOW_S3_ENDPOINT_URL=`
            1. Scroll upper and you will see bar with “Origin Endpoint” and adress. Copy it
            2. Pass it to your .env and erase bucket name from address. E.g:
                1. You copied https://your-bucket-name.fra1.digitaloceanspaces.com
                2. You should pass https://fra1.digitaloceanspaces.com
        5. `MLFLOW_TRACKING_URI=`
            1. Go to your project, find your droplet and copy IP
            2. Pass it to .env. E.g
                1. Before: MLFLOW_TRACKING_URI=http://<your_ip>:5000
                2. After: MLFLOW_TRACKING_URI=http://68.123.53.250:5000
        6. Click ctrl + x, type y, push enter. You done with .env
        7. Type `python3 [main.py](http://main.py)` and wait for installation, it should end without errors
        8. Type ./run_example.sh to start test experiment

4. ## Starting with MLFlow
    1. Go to your browser and find `<ip-of-your-droplet>:5000` (MLFlow works on port 5000)

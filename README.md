# Omdena_Hackathon_blog_writer-vijay
multi agent based simple project where it write a blog on given topic and it will provide option to download it as word document.
##1. Clone the repository
git clone https://github.com/vijayakrishna92/Omdena_Hackathon_blog_writer-vijay.git 

cd your-app-project

2. Create a Virtual Environment
To create a virtual environment, run the following command:

python -m venv any_name

This will create a folder with the name you provided (any_name).
3. Activate the Virtual Environment
Navigate to the Scripts folder inside the virtual environment. Drag and drop the activate file into your terminal, or use the following command:

.\any_name\Scripts\activate

4. Create a .env file
Inside the project folder, create a .env file and add your Hugging Face API key:

HUGGINGFACE_API_KEY=hf_yourapikeyhere

5. Install Required Packages
Install all the necessary packages by running:

pip install -r requirements.txt

6. Run the Application
Start the Streamlit app by running:

streamlit run main.py

This will open a local instance of the web app in your default browser.

Additional Notes
Make sure you have Hugging Face account to obtain the API key.

License
Include the license details if needed.

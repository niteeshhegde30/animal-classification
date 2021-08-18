#Code for Web app using Streamlit to show the demonstration during presentation
#Also code for web app without front page using Flask
#As we are using Flask webapp to actually implementing the required functionality,
# not to demonstrate, front end is not developed
# To use Streamlit webapp, comment the Flask api and app part and uncomment
# main() in __main__ 



#Import the necessary packages, functions and library
from trained_model import predict_the_image 
from messaging import sendMessage
from flask import Flask, request, jsonify
import streamlit as st 
from PIL import Image
import os

#to use streamlit webapp, comment the below codes till main()
#create flask app using Flask class
app = Flask(__name__)

# #define the endpoint and implement function to get the image, process it using
# #predict_the_image function of trained_model
# @app.route("/predict", methods=["POST"])
# def process_image():
#     file = request.files['image']
#     file.save('im-received.jpg')
#     animal_name=predict_the_image("im-received.jpg")
#     print(animal_name)
#     sendMessage(animal_name)
#     return jsonify({'msg': 'success', 'animal': animal_name})


#core function of streamlit webapp
def main():
    

	"""Animal Detection App"""
	#heading and description
	st.title("Wild Animals Classification")
	st.text("Build with Streamlit, Keras and Tensorflow")

	#defining two functionality, one to obtain and process image
	#another to breif about the project
	activities = ["Detection","About"]
	choice = st.sidebar.selectbox("Select Activty",activities)

	#implementing the image processing functionality
	#get the image, process using predict_the_image function of trained_model
	#send offline sms to the farmer to farmer to notify him about intrusion
	if choice == 'Detection':
		st.subheader("Animal detection")

		image_file = st.file_uploader("Upload Image",type=['jpg','png','jpeg'])

		if image_file is not None:
			our_image = Image.open(image_file)
			st.text("Original Image")
			file_details = {"FileName":image_file.name,"FileType":image_file.type}
			st.write(file_details)
			with open(os.path.join("gotimage.jpg"),"wb") as f: 
				f.write(image_file.getbuffer())         
			st.success("Saved File")
			st.image(our_image)
			animal=predict_the_image("gotimage.jpg")
			st.subheader("Animal in the Image: "+animal)
			sendMessage(animal)
			st.text("Message sent to farmer")


	#breif information about the project and context	
	elif choice == 'About':
		st.subheader("About Animal Classification App")
		st.markdown("Built with Streamlit, Tensorflow, Keras ")
		st.text("By Niteesh, Prasanna, Adarsh and Prajwal")
		st.success("DT lab prototype")


#uncomment the main() line, comment app.run() line to get streamlit webapp
if __name__ == '__main__':
    main()
    # app.run(debug=True)
    
#use streamlit run app_name command to run the webapp in browser
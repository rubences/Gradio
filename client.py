from gradio_client import Client

client = Client("abidlabs/whisper-large-v2")  # connecting to a Hugging Face Space
client.predict("test.mp4", api_name="/predict")


client = Client("https://bec81a83-5b5c-471e.gradio.live")  # connecting to a temporary Gradio share URL
job = client.submit("hello", api_name="/predict")  # runs the prediction in a background thread
job.result()

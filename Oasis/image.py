import base64
import requests
import os
import time

created = 0

def imagine(idea):

    api_keys = ["sk-F8qibFPGr29ndSslyszgxU27ymSNpwPco9BByn3JCJt5pEQZ","sk-uPlGt01yl0kt0aox6HBC0YtygGOjL5KPtyFRFacgqCFE43ZM",
                "sk-k9oDeYtXb15xnTuhA3sqLsY1ixfoTJLvy9fy1y4khoZi9Kxs","sk-jHXHU0D3ncVry0qd8uuSybuHkshgi4YefcfoOStV3dKyU5vW",
                      "sk-RarzWIa1Tu3r8nOhSDGWMCbjjeEGGeX57A1cnIAHS2e5OWEf","sk-x6V9EVsFFm7aoDzXO6FvHzWumPqeXVHHXPBtDxiprsAiQzoS",
                      "sk-2xJeDzXyFaKhChBvLaDmwRmf83njKe4seY7PkGKkHqli18TO","sk-t5nq5wwQtRtTQ6iQJ19kxd0HE7oL6F1w5TYDIDqLEAQFIoc8",
                      "sk-j17bCw84H50F3ZGPhd2SPXrsB67lmc63lQDV7LTuLSTpynpC","sk-OoLgNe2PV1ktcmTdLiQquFw5HrwwloyBIYaxq76m9AJ9indT",
                      "sk-MJNWCPwBWw1RPyYHAzm6v4uJtQm1k9C7izpQl4IZsskQpGgl","sk-JsK250BMZ5MR1a10rIoVkfOPwQm40bleBifWdmBnEhGvXGvs",
                      "sk-ZPJQQ66gYg1gnv2yINgrD02KM4RnYyfSJ9kfdD7klPZAAXEL","sk-yY2BwQObRjPJ9nttoHOIg2RG8qrq018PmsT5zvk7NtsQudJz",
                      "sk-NTMZYaZVrzAiAzzszBkB2I4ayIYmhi5yj7svTOtxhrw55JCl","sk-hBuHFpmFqcmx5lOefzx7jZhNGGpUB0QajkCWFX1vGXEeYa1F",
                      "sk-wiLBQ35t9SGwH4kuJdFLNRjfZG8EBgc3ggbXsD3UTSfWMAQo","sk-E4wrzWCORpOCx8We25qZ7TLVrfBwkhPaYq61OXm8NupHKfpS"]
    global created
    url = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image"

    body = {
        "steps": 40,
        "width": 1024,
        "height": 1024,
        "seed": 0,
        "cfg_scale": 5,
        "samples": 1,
        "text_prompts": [
            {
                "text": idea,
                "weight": 1
            },
            {
                "text": "blurry, bad, no realistic",
                "weight": -1
            }
        ],
    }

    for api_key in api_keys:
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": api_key,
        }

        try:
            response = requests.post(
                url,
                headers=headers,
                json=body,
            )

            if response.status_code != 200:
                error_message = response.json()["message"]
                if "not have enough balance" in error_message:
                    raise Exception("API key does not have enough balance to make the request.")
                else:
                    raise Exception(error_message)

            data = response.json()

            # make sure the out directory exists
            if not os.path.exists("./imagine"):
                os.makedirs("./imagine")

            for i, image in enumerate(data["artifacts"]):

                with open(f'./imagine/' + idea.replace(' ','_') + '.png', "wb") as f:
                    f.write(base64.b64decode(image["base64"]))
                image_path = 'imagine\\'+ idea.replace(' ','_') + '.png'
                os.startfile(image_path)

            # return idea.replace(' ','_')
            return "Image Created Successfully"

        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            time.sleep(5)  # Wait for 5 seconds before retrying with the next API key
        except Exception as e:
            # print(f"Error: {e}")
            # Handle the specific exception where the API key does not have enough balance here
            if "API key does not have enough balance" in str(e):
                continue  # Move on to the next API key
            else:
                return "Failed to create image."

    return "Failed to create image. All API keys exhausted or internet connection issue."



import openai
import json
import requests
import yfinance as yfn
import misc
import open_close
import image

openai.api_key="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"
weather_key = 'eff344c0be61d1a7863ecd99c0510a38'

def weather(place):
    data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={place}&units=metric&APPID={weather_key}")


    if data.json()['cod'] == '404':
        report=f"We cann't find the given location or place make sure you typed it correctly"
    else:
        weather = data.json()['weather'][0]['main']
        
        temp = round(data.json()['main']['temp'])

        weather_details=f"The weather in {place} is: {weather}"
        temp_details=f"The temperature in {place} is: {temp}ºC"
        report = weather_details + " " + temp_details
    return report
def stock(comp_symb):
    return str(yfn.Ticker(comp_symb).history(period="1mo").iloc[-1].Close)


oasis="your name is oasis, you are a virtual assistant. devoloped by codeforgers. codeforgers are group of students of iitm college. iitm stands for institute of information technology & managment which is affliated by GGSIPU University... you are an language model that is create by codeforgers.there are 6 members in codeforgers, zishan, kunal Rajput,kartik Singhal,krit Barnwal,sachin soni and shreshta sharama.."
cat="just replace the answer with the word meow, you are a cat , if the answer is hello how are you, you replace the word with meow your answer will be meow meow meow"


role=oasis
content = [{"role": "system", "content": role},]
def generative_ai(inquire):
    CHAT="win"
    content.append({"role": "user", "content": inquire})
    user_functions = [
        {
            "name": "retrieve_stock_price",
            "description": "Retrieve the present share value of a corporation using its company symbol (comp_symb) or simply ticker ",
            "parameters": {
                "type": "object",
                "properties": {
                    "comp_symb": {
                        "type": "string",
                        "description": "The comp_symb is a is replacement word for ticker a that is a symbol of a company in share market",
                    },
                
                },
                "required": ["comp_symb"],
            },
        },{
            "name": "retrieve_weather_details",
            "description": "Obtain the current climate conditions in a specified locality, province, or town. or Fetch the present meteorological status in a particular area, region, or municipality. using place ",
            "parameters": {
                "type": "object",
                "properties": {
                    "place": {
                        "type": "string",
                        "description": "place is used to describe the locatin of which we want to retrieve the weather condition",
                    },
                
                },
                "required": ["place"],
            },
        }
    ]
    try:
        
        report = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=content,
            functions=user_functions,
            function_call="auto", 
        )

        report_message = report["choices"][0]["message"]

        if report_message.get("function_call"):
            
            predefined_user_functions = {
                "retrieve_weather_details": weather,
                "retrieve_stock_price": stock,
            }  
            avalaible_method_name = report_message["function_call"]["name"]
            method_that_calls = predefined_user_functions[avalaible_method_name]
            arguments_of_methods = json.loads(report_message["function_call"]["arguments"])
            if avalaible_method_name=="retrieve_weather_details":
                function_report = method_that_calls(
                    place=arguments_of_methods.get("place"),
                )
            if avalaible_method_name=="retrieve_stock_price":
                function_report = method_that_calls(
                    comp_symb=arguments_of_methods.get("comp_symb"),
                )
        
            content.append(report_message) 
            content.append(
                {
                    "role": "function",
                    "name": avalaible_method_name,
                    "content": function_report,
                }
            ) 
            
            second_report = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-0613",
                messages=content,
            ) 
            reply_message=second_report["choices"][0]["message"]["content"]
            content.append({"role": "assistant", "content": reply_message})
            return reply_message
        
    except openai.error.RateLimitError as e:
        return("RATE LIMITE EXCEED:\nPlease note that this is free version with limit of 3/min request\nPlease buy premium for uninterpted conversation")
              
    else:        
        try:
            reply = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=content,
            stream=False,
            )
            
            reply_message=reply["choices"][0]["message"]["content"]
            content.append({"role": "assistant", "content": reply_message})
            print(reply_message)
            return reply_message
        except openai.error.RateLimitError as e:
            return("RATE LIMITE EXCEED:\nPlease note that this is free version with limit of 3/min request\n Please buy premium for uninterpted conversation")
def main(command):        
    if any(word in command.split() for word in misc.launch):
        command = " ".join(word for word in command.split() if word not in misc.launch and word != "and")
        a=[open_close.open_app(x) for x in open_close.app_list if any(a in command.split() for a in x.split(" "))]
        if len(a)>0:
            return f"{a[0]}"
        else:
            return "nothing to be opened"
    if ("imagine" in command) or ("generate" in command) or ("create" in command):
        return image.imagine(command)
    else:
        return generative_ai(command)


    
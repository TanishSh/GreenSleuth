import openai
import speechToText
import audio
import maps

def report():
    openai.api_key = "KEY"
    filename = 'output.wav'
    audio.record_audio()
    # text = speechToText.speechToText(filename)     
    # print(text) 
    # messages = [{"role": "system", "content": "Assume you are working as emergency liner. Summarize the following information, extract the address and situation as bullet point (if it is ridiculous, returns: FAKE REPORT;):"}]    
    # messages.append({"role": "user", "content": text},)    
    # chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)    
    # text = str(chat.choices[0].message.content)   
    # print(text) 
    return """
    Address:
    - 350 Victoria St

    Situation:
    - Man armed with gun
    - Threatening to kill people
    """

def address(incident_report):
    print(incident_report)
    if "FAKE REPORT" in incident_report:
        return "Fake Report"
    if "Not enough information" in incident_report:
        return "Not enough information"
    relevant_text = incident_report[incident_report.find("Address")+9:incident_report.find("Situation")].replace(".", "").replace("-", "").strip()
    return maps.extract_address_coordinates(relevant_text), maps.map_link(relevant_text)

#response = inference("Hi")
# reporttext = report()
# print(address(reporttext))
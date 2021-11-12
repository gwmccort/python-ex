from requests_toolbelt.multipart
import decoder

testEnrollResponse = requests.post(...)
multipart_data = decoder.MultipartDecoder.from_response(testEnrollResponse)

for part in multipart_data.parts:
    print(part.content)  # Alternatively, part.text if you want unicode
print(part.headers)

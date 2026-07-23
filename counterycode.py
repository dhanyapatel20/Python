country_code = {'India' : '0091',

'Australia' : '0025',

'Nepal' : '00977'}

print("country code of India is : " + country_code['India'])
print("country code of Australia is : " + country_code['Australia'])
print("country code of Nepal is : " + country_code['Nepal'])
print("country code of Japan is : " + country_code.get("Japan", "Code not found"))
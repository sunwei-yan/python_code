import requests
import json
t2=''
import time

url="https://appc.baidu.com/uiserver?abi=armeabi-v7a&cen=cuid_cut_cua_uid_recommend_c3_aid&client_start=711587&recommend=t5xTz3q6B&action=topicboard&open_type=0&gms=false&sids=2158_2%2C2187_2&start_type=1&andr_d=2dcdc91e66c41b97&start_request=711588&md=SM-G988N&ndid=&id=102576&nt=1&login=0&bannert=26%4027%4028%4029%4030%4032%4043&apn=&apk_ver=16798398&usertype=0&bdgid=&client_version=9.6.0.0&start_from_source=6&pkname=com.baidu.appsearch&disp=z3qksx-user+5.1.1+NRD90M+500230106+release-keys&from=1022306n&bd=samsung&c3_aid=0avgNr9kvaJou3RhJk3chla7Q8pAtQOQp83yPrfovMJCi3M7z93-urt9QaJkA&pu=At1Jm4MJx%252FDVnI6o6XLXnFNsOqtUzplspTxzJHdP%252BM4nMXix9TGqOcMQJ1AFX2m7kBseECvluJwL%250Aj2%252FJur4Z0N%252BbwnrG48pRdkTaasMPjDgZNuVCPrxLgOx1mB3BANnZgP2lWkYsWMW%252F2PrTatOhs1om%250Afrg1kLlFXaKZMChKdndnpEGCpJq926uYmhcQTUUPjtyPaUTkXIbIoa1GEexBpyBTmhk4rYY6yVz2%250An2SDEA%252Fx%252FB5iLfnPoi4chrwIDz2ubPoLw%252BeRO02xUD89R9l25%252FJt7Q8IMXmDUPc1vkZAj%252FOa9QpG%250ARvCfiYfGwbLI8tzYhtbV%252B1vX0bywhVA0RoCfdsfo4klxYi1VZTdEP4HUVhsgh9kb3PU4t2jWCn5l%250AL%252Bh9C9hqpz%252F06bUXmcVGEGdqSBytPHl1nb9cKZaRFeikCYEz9f1Y8BLcKj6UF7b0pZJro5H5oylR%250AndsuPMhfODaWX1sKDq%252F5BuCselpbJTr6JqsZ7m8WyUxE33H3kAAnMhxjShOjp3DabVWyaCxXvPpN%250AmoHASIO0zOFQd0rRSkmvc0zlSCah26ftUx1c4Wu2iTAL1XqG7dKDF9JxDaaUUbGkfE5LaZoANSDn%250A0oK4rOLnsO7T7lgsQ63u7ki8oXnF25gz0MT6yL0Aq0dfIZud2DU9loOKMDeMIGpXgQTyVAhiNNAQ%250AxbOrwe62okHU7Fzi8F7qh5Z%252BSe5Eqd4cCO65BLKjgpMFB7sB2bqDPcVUAQzsL9JcpnV7%252FXce8qwb%250AyUellRc99NMTFwInlyJ%252B2boxFLTs%252BWn3wdnvMiQzvt2%252Bcfi8%252BI4GFkGsT7wtonfDMTtrUfe7%252FlUT%250AasiplNkM5eG6%252BAFJtN2X%252BGtqTC9BjWQ5YlptOoyr9bTk82SMMLPj%252BxdNSqIUcK2W%252BJb5G1KFG8Bd%250AoEuApGpXD%252B0iYoZ%252FG0yrL2j%252FHMnG5tf5MH%252FRpPKmgWfsQq8EghD%252BNCZtiz0SMgnZmPRQXy5waIBG%250AC3pidZcb4uXSef83TwIx1KnuMaXYp%252Fj7ZriwXXgrmYgpNWtjxB9m33Oyow%253D%253D&network=WF&mount=2&os_ver=5.1.1&country=CN&psize=3&is_support_webp=true&pn=0&f=spectacle%2Bselected%40topic%40topicid%2B102576&uid=0avai_a5HajVi-ul08298_87SalLa28n_aH-i_uS-8q4uHRvr9DgupiTWMq6C&language=zh&start_query=&platform_version_id=22&ver=16798398&scene=home_index&ptl=hps&crid=1676880245806%20HTTP/1.1"

header={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
resp=requests.get(url=url,headers=header)
s=json.loads(resp.text)
t1=s["result"]["data"][0]["itemdata"]['developername']

print(t1)

  
time.sleep(1)

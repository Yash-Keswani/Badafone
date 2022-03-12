import csv
import random
from random import sample
from csv import DictWriter, DictReader

import lorem_text.lorem

cities = ['Delhi', 'Mumbai', 'Kolkāta', 'Bangalore', 'Chennai', 'Hyderābād', 'Pune', 'Ahmedabad', 'Sūrat', 'Lucknow', 'Jaipur', 'Cawnpore', 'Mirzāpur', 'Nāgpur', 'Ghāziābād', 'Indore', 'Vadodara', 'Vishākhapatnam', 'Bhopāl', 'Chinchvad', 'Patna', 'Ludhiāna', 'Āgra', 'Kalyān', 'Madurai', 'Jamshedpur', 'Nāsik', 'Farīdābād', 'Aurangābād', 'Rājkot', 'Meerut', 'Jabalpur', 'Thāne', 'Dhanbād', 'Allahābād', 'Vārānasi', 'Srīnagar', 'Amritsar', 'Alīgarh', 'Bhiwandi', 'Gwalior', 'Bhilai', 'Hāora', 'Rānchi', 'Bezwāda', 'Chandīgarh', 'Mysore', 'Raipur', 'Kota', 'Bareilly', 'Jodhpur', 'Coimbatore', 'Dispur', 'Guwāhāti', 'Solāpur', 'Trichinopoly', 'Hubli', 'Jalandhar', 'Bhubaneshwar', 'Bhayandar', 'Morādābād', 'Kolhāpur', 'Thiruvananthapuram', 'Sahāranpur', 'Warangal', 'Salem', 'Mālegaon', 'Kochi', 'Gorakhpur', 'Shimoga', 'Tiruppūr', 'Guntūr', 'Raurkela', 'Mangalore', 'Nānded', 'Cuttack', 'Chānda', 'Dehra Dūn', 'Durgāpur', 'Āsansol', 'Bhāvnagar', 'Amrāvati', 'Nellore', 'Ajmer', 'Tinnevelly', 'Bīkaner', 'Agartala', 'Ujjain', 'Jhānsi', 'Ulhāsnagar', 'Davangere', 'Jammu', 'Belgaum', 'Gulbarga', 'Jāmnagar', 'Dhūlia', 'Gaya', 'Jalgaon', 'Kurnool', 'Udaipur', 'Bellary', 'Sāngli', 'Tuticorin', 'Calicut', 'Akola', 'Bhāgalpur', 'Sīkar', 'Tumkūr', 'Quilon', 'Muzaffarnagar', 'Bhīlwāra', 'Nizāmābād', 'Bhātpāra', 'Kākināda', 'Parbhani', 'Pānihāti', 'Lātūr', 'Rohtak', 'Rājapālaiyam', 'Ahmadnagar', 'Cuddapah', 'Rājahmundry', 'Alwar', 'Muzaffarpur', 'Bilāspur', 'Mathura', 'Kāmārhāti', 'Patiāla', 'Saugor', 'Bijāpur', 'Brahmapur', 'Shāhjānpur', 'Trichūr', 'Barddhamān', 'Kulti', 'Sambalpur', 'Purnea', 'Hisar', 'Fīrozābād', 'Bīdar', 'Rāmpur', 'Shiliguri', 'Bāli', 'Pānīpat', 'Karīmnagar', 'Bhuj', 'Ichalkaranji', 'Tirupati', 'Hospet', 'Āīzawl', 'Sannai', 'Bārāsat', 'Ratlām', 'Handwāra', 'Drug', 'Imphāl', 'Anantapur', 'Etāwah', 'Rāichūr', 'Ongole', 'Bharatpur', 'Begusarai', 'Sonīpat', 'Rāmgundam', 'Hāpur', 'Uluberiya', 'Porbandar', 'Pāli', 'Vizianagaram', 'Puducherry', 'Karnāl', 'Nāgercoil', 'Tanjore', 'Sambhal', 'Naihāti', 'Secunderābād', 'Kharagpur', 'Dindigul', 'Shimla', 'Ingrāj Bāzār', 'Ellore', 'Puri', 'Haldia', 'Nandyāl', 'Bulandshahr', 'Chakradharpur', 'Bhiwāni', 'Gurgaon', 'Burhānpur', 'Khammam', 'Madhyamgram', 'Ghāndīnagar', 'Baharampur', 'Mahbūbnagar', 'Mahesāna', 'Ādoni', 'Rāiganj', 'Bhusāval', 'Bahraigh', 'Shrīrāmpur', 'Tonk', 'Sirsa', 'Jaunpur', 'Madanapalle', 'Hugli', 'Vellore', 'Alleppey', 'Cuddalore', 'Deo', 'Chīrāla', 'Machilīpatnam', 'Medinīpur', 'Bāramūla', 'Chandannagar', 'Fatehpur', 'Udipi', 'Tenāli', 'Sitalpur', 'Conjeeveram', 'Proddatūr', 'Navsāri', 'Godhra', 'Budaun', 'Chittoor', 'Harīpur', 'Saharsa', 'Vidisha', 'Pathānkot', 'Nalgonda', 'Dibrugarh', 'Bālurghāt', 'Krishnanagar', 'Fyzābād', 'Silchar', 'Shāntipur', 'Hindupur', 'Erode', 'Jāmuria', 'Hābra', 'Ambāla', 'Mauli', 'Kolār', 'Shillong', 'Bhīmavaram', 'New Delhi', 'Mandsaur', 'Kumbakonam', 'Tiruvannāmalai', 'Chicacole', 'Bānkura', 'Mandya', 'Hassan', 'Yavatmāl', 'Pīlibhīt', 'Pālghāt', 'Abohar', 'Pālakollu', 'Kānchrāpāra', 'Port Blair', 'Alīpur Duār', 'Hāthras', 'Guntakal', 'Navadwīp', 'Basīrhat', 'Hālīsahar', 'Rishra', 'Dharmavaram', 'Baidyabāti', 'Darjeeling', 'Sopur', 'Gudivāda', 'Adilābād', 'Titāgarh', 'Chittaurgarh', 'Narasaraopet', 'Dam Dam', 'Vālpārai', 'Osmānābād', 'Champdani', 'Bangaon', 'Khardah', 'Tādpatri', 'Jalpāiguri', 'Suriāpet', 'Tādepallegūdem', 'Bānsbāria', 'Negapatam', 'Bhadreswar', 'Chilakalūrupet', 'Kalyani', 'Gangtok', 'Kohīma', 'Khambhāt', 'Aurangābād', 'Emmiganūr', 'Rāyachoti', 'Kāvali', 'Mancherāl', 'Kadiri', 'Ootacamund', 'Anakāpalle', 'Sirsilla', 'Kāmāreddipet', 'Pāloncha', 'Kottagūdem', 'Tanuku', 'Bodhan', 'Karūr', 'Mangalagiri', 'Kairāna', 'Mārkāpur', 'Malaut', 'Bāpatla', 'Badvel', 'Jorhāt', 'Koratla', 'Pulivendla', 'Jaisalmer', 'Tādepalle', 'Armūr', 'Jatani', 'Gadwāl', 'Nagari', 'Wanparti', 'Ponnūru', 'Vinukonda', 'Itānagar', 'Tezpur', 'Narasapur', 'Kothāpet', 'Mācherla', 'Kandukūr', 'Sāmalkot', 'Bobbili', 'Sattenapalle', 'Vrindāvan', 'Mandapeta', 'Belampalli', 'Bhīmunipatnam', 'Nāndod', 'Pithāpuram', 'Punganūru', 'Puttūr', 'Jalor', 'Palmaner', 'Dholka', 'Jaggayyapeta', 'Tuni', 'Amalāpuram', 'Jagtiāl', 'Vikārābād', 'Venkatagiri', 'Sihor', 'Jangaon', 'Mandamāri', 'Metpalli', 'Repalle', 'Bhainsa', 'Jasdan', 'Jammalamadugu', 'Rāmeswaram', 'Addanki', 'Nidadavole', 'Bodupāl', 'Rājgīr', 'Rajaori', 'Naini Tal', 'Channarāyapatna', 'Maihar', 'Panaji', 'Junnar', 'Amudālavalasa', 'Damān', 'Kovvūr', 'Solan', 'Dwārka', 'Pathanāmthitta', 'Kodaikānal', 'Udhampur', 'Giddalūr', 'Yellandu', 'Shrīrangapattana', 'Angamāli', 'Umaria', 'Fatehpur Sīkri', 'Mangūr', 'Pedana', 'Uran', 'Chimākurti', 'Devarkonda', 'Bandipura', 'Silvassa', 'Pāmidi', 'Narasannapeta', 'Jaynagar-Majilpur', 'Khed Brahma', 'Khajurāho', 'Koilkuntla', 'Diu', 'Kulgam', 'Gauripur', 'Abu', 'Curchorem', 'Kavaratti', 'Panchkula', 'Kagaznāgār']

tower = []
for i in range(1, 200):
	tower.append({"tower_ID": i, "city": cities[i]})
with open("tower.csv", "w", encoding='utf-8', newline='\n') as fl:
	towrite = DictWriter(fl, ["tower_ID", "city"])
	towrite.writeheader()
	towrite.writerows(tower)

with open("names.csv",encoding='utf-8', newline='\n') as fl:
	toread = DictReader(fl)
	names = list(toread)
"""
wecare = sample(names, 400)
with open("names.csv", "w", encoding='utf-8', newline='\n') as fl:
	towrite = DictWriter(fl, wecare[0].keys())
	towrite.writeheader()
	towrite.writerows(wecare)
"""
customers = []
aadhaars = sample(range(10**12, 10**13), 400)
IDs = sample(range(100000), 400)
for i, user in enumerate(names):
	customer = {
		"ID": IDs[i],
		"name": user["name"],
		"phone_number": random.randrange(7*10**10, 10**11),
		"sex": user["gender"],
		"aadhaar": aadhaars[i],
		"email": "_".join(user["name"].split(" "))+"@gmail.com",
		"birthdate": f"{random.randrange(1985,2004)}-{random.randrange(1, 12)}-{random.randrange(1,28)}"
	}
	customers.append(customer)

with open("customers.csv", "w", encoding='utf-8', newline='\n') as fl:
	towrite = DictWriter(fl, customers[0].keys())
	towrite.writeheader()
	towrite.writerows(customers)

sim_cards = []
for user in customers:
	home_tower = random.choice(tower)["tower_ID"]
	t = random.randrange(1, 100)
	sim_card = {
		"phone_number": user["phone_number"],
		"activated": 1 if random.randrange(1, 100) < 90 else 0,
		"date_of_activation": f"{random.randrange(2017,2021)}-{random.randrange(1, 12)}-{random.randrange(1,28)}",
		"home_tower": home_tower,
		"current_tower": home_tower if t < 80 else random.choice(tower)["tower_ID"],
		"roaming": 1 if t >= 80 else 0
	}
	sim_cards.append(sim_card)

with open("SIM_Cards.csv", "w+", encoding='utf-8', newline='\n') as fl:
	towrite = DictWriter(fl, sim_cards[0].keys())
	towrite.writeheader()
	towrite.writerows(sim_cards)

ticketers = random.sample([x["ID"] for x in customers], 100)

with open("Employee.csv", encoding='utf-8', newline='\n') as fl:
	employees = list(csv.DictReader(fl))

tickets = []
ticket_IDs = random.sample(range(1, 10000), 100)
employee_IDs = random.sample(employees, 100)
for i, x in enumerate(ticketers):
	ticket = {
		"ticket_ID": ticket_IDs[i],
		"customer_ID": x,
		"employee_ID": employee_IDs[i]["employee_id"],
		"content": lorem_text.lorem.words(25),
		"category": random.choice(['Calling Help', 'Data Help', 'Connectivity Issues', 'Plan Enquiry', 'Payment Enquiry']),
		"closed": 0 if random.randint(1, 100) < 90 else 1
	}
	tickets.append(ticket)

with open("tickets.csv", "w+", encoding='utf-8', newline='\n') as fl:
	towrite = DictWriter(fl, tickets[0].keys())
	towrite.writeheader()
	towrite.writerows(tickets)

phone_nums = [x["phone_number"] for x in sim_cards]

SMSs = []
for i in range(500):
	SMS = {
		"sender": random.choice(phone_nums),
		"send_time": f"{random.randint(0, 23)}:{random.randint(0, 59)}:{random.randint(0,59)}",
		"receiver": random.choice(phone_nums),
		"read": 1 if random.randint(0, 100) < 70 else 0
	}
	SMSs.append(SMS)
	
with open("SMSs.csv", "w+", encoding='utf-8', newline='\n') as fl:
	towrite = DictWriter(fl, SMSs[0].keys())
	towrite.writeheader()
	towrite.writerows(SMSs)

with open("w.csv", newline='\n') as fl:
	wl = list(DictReader(fl, delimiter='\t'))

wallets = []
for i, W in enumerate(wl):
	wallet = {
		"phone_number": phone_nums[i],
		"payment_method": W["preferred_payment_method"],
		"balance": W["balance"]
	}
	wallets.append(wallet)

with open("wallet.csv", "w+", encoding='utf-8', newline='\n') as fl:
	towrite = DictWriter(fl, wallets[0].keys())
	towrite.writeheader()
	towrite.writerows(wallets)
	
with open("tr.csv", newline='\n') as fl:
	tr = list(DictReader(fl))

transactions = []
for i, W in enumerate(tr):
	transaction = {
		"phone_number": phone_nums[i],
		"payment_method": W["purchase_time"],
		"plan_ID": W["plan_id"]
	}
	transactions.append(transaction)

with open("transactions.csv", "w+", encoding='utf-8', newline='\n') as fl:
	towrite = DictWriter(fl, transactions[0].keys())
	towrite.writeheader()
	towrite.writerows(transactions)

calls = []
for i in range(500):
	entities = random.sample(phone_nums, 2)
	towers = [x["tower_ID"] for x in random.sample(tower, 2)]
	call = {
		"caller": entities[0],
		"callee": entities[1],
		"caller_tower": towers[0],
		"callee_tower": towers[1],
		"start_time": f"{random.randint(0, 23)}:{random.randint(0, 59)}:{random.randint(0,59)}",
		"end_time": f"{random.randint(0, 23)}:{random.randint(0, 59)}:{random.randint(0,59)}"
	}
	calls.append(call)

with open("calls.csv", "w+", encoding='utf-8', newline='\n') as fl:
	towrite = DictWriter(fl, calls[0].keys())
	towrite.writeheader()
	towrite.writerows(calls)

subscriptions = []
for i in phone_nums:
	plans = []
	decider = random.randint(0, 100)
	if decider > 40:
		plans = random.sample(range(1, 31), 2)
	else:
		plans = [random.choice(range(1, 31))]
	
	for plan in plans:
		subscription = {
			"phone_number": i,
			"plan_ID": plan
		}
		subscriptions.append(subscription)

with open("subscriptions.csv", "w+", encoding='utf-8', newline='\n') as fl:
	towrite = DictWriter(fl, subscriptions[0].keys())
	towrite.writeheader()
	towrite.writerows(subscriptions)

with open("pc.csv", newline='\n') as fl:
	pc = list(DictReader(fl))

usages = []
for i, num in enumerate(phone_nums):
	pc[i]["phone_number"] = num
	# test = pc[i]["start_date"].split("/")
	# if len(test) == 1:
	# 	test = test[0].split("-")
	# p c[i]["start_date"] = test[2]+"-"+test[1]+"-"+test[0]
	usages.append(pc[i])

with open("callusage.csv", "w+", encoding='utf-8', newline='\n') as fl:
	towrite = DictWriter(fl, usages[0].keys())
	towrite.writeheader()
	towrite.writerows(usages)

with open("dt.csv", newline='\n') as fl:
	pc = list(DictReader(fl))

usages = []
for i, num in enumerate(phone_nums):
	pc[i]["phone_number"] = num
	usages.append(pc[i])

with open("datausage.csv", "w+", encoding='utf-8', newline='\n') as fl:
	towrite = DictWriter(fl, usages[0].keys())
	towrite.writeheader()
	towrite.writerows(usages)

def gov_7(cin):
    green_db = ["Australia", "Bahrain", "Canada", "Chile", "Colombia", "Costa Rica", "Dominican Republic", "Ecuador",
                "El Salvador", "Austria", "Bulgaria", "Belgium", "Czech Republic", "Cyprus", "Croatia", "Denmark",
                "Estonia", "Finland", "France", "Germany", "Greece", "Hungary", "Italy", "Ireland", "Latvia",
                "Luxembourg", "Malta", "Netherlands", "Lithuania", "Poland", "Portugal", "Romania", "Spain", "Slovakia",
                "Sweden", "Slovenia", "European Union", "Honduras", "Hong Kong", "Israel", "Laos", "Malaysia", "Mexico",
                "New Zealand", "Oman", "Panama", "Peru", "Singapore", "South Africa", "Switzerland", "Taiwan",
                "United Kingdom"]
    yellow_db = ["Bolivia", "Brazil", "Brunei", "Cote d'Ivoire", "Egypt", "Ghana", "Guatemala", "India", "Indonesia",
                 "Japan", "Jordan", "Kenya", "Kuwait", "Morocco", "Nicaragua", "Norway", "Pakistan", "Paraguay",
                 "Qatar",
                 "South Korea", "Thailand", "The Philippines", "Tunisia", "Turkey", "Ukraine", "United Arab Emirates"]
    red_db = ["Algeria", "Angola", "Argentina", "Bangladesh", "Cambodia", "China", "Ethiopia", "Myanmar (Burma)",
              "Nigeria", "Russia", "Saudi Arabia", "Vietnam", "Venezuela"]

    countries = {
        "Algeria": "The company does business in Algeria. Algeria imposes barriers to trade including customs delays, "
                   "data localization requirements, and an investment law that mandates Algerian ownership of at least "
                   "51% in all projects involving foreign investments.",
        "Angola": "The company does business in Angola. Angola imposes barriers to trade including bans on imports of "
                  "certain goods, foreign exchange controls, and investment barriers.",
        "Argentina": "The company does business in Argentina. Argentina imposes barriers to trade including foreign "
                     "exchange and capital controls.",
        "Australia": "The company does business in Australia. Australia maintains few barriers to trade in goods and "
                     "services and few restrictions on foreign capital flows and investment.",
        "Bahrain": "The company does business in Bahrain. Bahrain maintains few barriers to trade in goods and "
                   "services and few restrictions on foreign capital flows and investment.",
        "Bangladesh": "The company does business in Bangladesh. Bangladesh imposes barriers to trade including "
                      "prohibitions on foreign involvement in certain economic sectors, investment restrictions, and a "
                      "lack of enforcement against anticompetitive conduct.",
        "Bolivia": "The company does business in Bolivia. Bolivia imposes barriers to trade including investment "
                   "barriers in strategic sectors, restrictions on the level of foreign employees, and limit on "
                   "foreign companies’ access to international arbitration in cases of conflicts with the government.",
        "Brazil": "The company does business in Brazil. Brazil imposes barriers to trade including bans on certain "
                  "imported goods and double taxation of imports.",
        "Brunei": "The company does business in Brunei. Brunei imposes barriers to trade including localization "
                  "requirements, a lack of transparency, and a restriction on foreign land ownership.",
        "Cambodia": "The company does business in Cambodia. Cambodia imposes barriers to trade including arbitrary "
                    "customs enforcement, restrictions on foreign ownership of property, and widespread smuggling.",
        "Canada": "The company does business in Canada. Canada maintains few barriers to trade in goods and services "
                  "and few restrictions on foreign capital flows and investment.",
        "Chile": "The company does business in Chile. Chile maintains few barriers to trade in goods and services and "
                 "few restrictions on foreign capital flows and investment.",
        "China": "The company does business in China. China imposes barriers to trade including forced technology "
                 "transfer, limited market access, and investment restrictions.",
        "Colombia": "The company does business in Colombia. Colombia maintains few barriers to trade in goods and "
                    "services and few restrictions on foreign capital flows and investment.",
        "Costa Rica": "The company does business in Costa Rica. Costa Rica imposes barriers to trade including an "
                      "inconsistent regulatory environment for investment.",
        "Cote d'Ivoire": "The company does business in Cote d'Ivoire. Cote d'Ivoire imposes barriers to trade "
                         "including a lack of regulatory transparency and bans on the import of certain goods.",
        "Dominican Republic": "The company does business in the Dominican Republic. The Dominican Republic "
                              "maintains few barriers to trade in goods and services and few restrictions on "
                              "foreign capital flows and investment.",
        "Ecuador": "The company does business in Ecuador. Ecuador maintains few barriers to trade in goods and "
                   "services and few restrictions on foreign capital flows and investment.",
        "Egypt": "The company does business in Egypt. Egypt imposes barriers to trade including costly and "
                 "delayed customs processing, restrictions on foreign equity in certain sectors, and a mandate "
                 "that 60% of senior executives be Egyptian citizens at information technology (IT) companies.",
        "El Salvador": "The company does business in El Salvador. El Salvador maintains few barriers to trade "
                       "in goods and services and few restrictions on foreign capital flows and investment.",
        "Ethiopia": "The company does business in Ethiopia. Ethiopia maintains barriers to trade including "
                    "a complex import licensing regime, strict foreign exchange controls, and monopoly control "
                    "over various sectors by State-owned enterprises (SOE).",
        "Austria": "The company does business in Austria, which is a member of the European Union (EU). The EU "
                   "imposes barriers to trade including data localization requirements that hinder cross-border "
                   "trade and extensive subsidies to the European aerospace industry.",
        "Bulgaria": "The company does business in Bulgaria, which is a member of the European Union (EU). The EU "
                    "imposes barriers to trade including data localization requirements that hinder cross-border trade "
                    "and extensive subsidies to the European aerospace industry.",
        "Belgium": "The company does business in Belgium, which is a member of the European Union (EU). The EU imposes "
                   "barriers to trade including data localization requirements that hinder cross-border trade and "
                   "extensive subsidies to the European aerospace industry.",
        "Czech Republic": "The company does business in the Czech Republic, which is a member of the European "
                          "Union (EU). The EU imposes barriers to trade including data localization requirements "
                          "that hinder cross-border trade and extensive subsidies to the European aerospace industry.",
        "Cyprus": "The company does business in Cyprus, which is a member of the European Union (EU). The EU imposes "
                  "barriers to trade including data localization requirements that hinder cross-border trade and "
                  "extensive subsidies to the European aerospace industry.",
        "Croatia": "The company does business in Croatia, which is a member of the European Union (EU). The EU imposes "
                   "barriers to trade including data localization requirements that hinder cross-border trade and "
                   "extensive subsidies to the European aerospace industry.",
        "Denmark": "The company does business in Denmark, which is a member of the European Union (EU). The EU imposes "
                   "barriers to trade including data localization requirements that hinder cross-border trade and "
                   "extensive subsidies to the European aerospace industry.",
        "Estonia": "The company does business in Estonia, which is a member of the European Union (EU). The EU imposes "
                   "barriers to trade including data localization requirements that hinder cross-border trade and "
                   "extensive subsidies to the European aerospace industry.",
        "Finland": "The company does business in Finland, which is a member of the European Union (EU). The EU imposes "
                   "barriers to trade including data localization requirements that hinder cross-border trade and "
                   "extensive subsidies to the European aerospace industry.",
        "France": "The company does business in France, which is a member of the European Union (EU). The EU imposes "
                  "barriers to trade including data localization requirements that hinder cross-border trade and "
                  "extensive subsidies to the European aerospace industry.",
        "Germany": "The company does business in Germany, which is a member of the European Union (EU). The EU imposes "
                   "barriers to trade including data localization requirements that hinder cross-border trade and "
                   "extensive subsidies to the European aerospace industry.",
        "Greece": "The company does business in Greece, which is a member of the European Union (EU). The EU imposes "
                  "barriers to trade including data localization requirements that hinder cross-border trade and "
                  "extensive subsidies to the European aerospace industry.",
        "Hungary": "The company does business in Hungary, which is a member of the European Union (EU). The EU imposes "
                   "barriers to trade including data localization requirements that hinder cross-border trade and "
                   "extensive subsidies to the European aerospace industry.",
        "Italy": "The company does business in Italy, which is a member of the European Union (EU). The EU imposes "
                 "barriers to trade including data localization requirements that hinder cross-border trade and "
                 "extensive subsidies to the European aerospace industry.",
        "Ireland": "The company does business in Ireland, which is a member of the European Union (EU). The EU imposes "
                   "barriers to trade including data localization requirements that hinder cross-border trade and "
                   "extensive subsidies to the European aerospace industry.",
        "Latvia": "The company does business in Latvia, which is a member of the European Union (EU). The EU imposes "
                  "barriers to trade including data localization requirements that hinder cross-border trade and "
                  "extensive subsidies to the European aerospace industry.",
        "Luxembourg": "The company does business in Luxembourg, which is a member of the European Union (EU). The EU "
                      "imposes barriers to trade including data localization requirements that hinder cross-border "
                      "trade and extensive subsidies to the European aerospace industry.",
        "Malta": "The company does business in Malta, which is a member of the European Union (EU). The EU imposes "
                 "barriers to trade including data localization requirements that hinder cross-border trade and "
                 "extensive subsidies to the European aerospace industry.",
        "Netherlands": "The company does business in the Netherlands, which is a member of the European Union (EU). "
                       "The EU imposes barriers to trade including data localization requirements that hinder "
                       "cross-border trade and extensive subsidies to the European aerospace industry.",
        "Lithuania": "The company does business in Lithuania, which is a member of the European Union (EU). "
                     "The EU imposes barriers to trade including data localization requirements that hinder "
                     "cross-border trade and extensive subsidies to the European aerospace industry.",
        "Poland": "The company does business in Poland, which is a member of the European Union (EU). The EU imposes "
                  "barriers to trade including data localization requirements that hinder cross-border trade and "
                  "extensive subsidies to the European aerospace industry.",
        "Portugal": "The company does business in Portugal, which is a member of the European Union (EU). The EU "
                    "imposes barriers to trade including data localization requirements that hinder cross-border "
                    "trade and extensive subsidies to the European aerospace industry.",
        "Romania": "The company does business in Romania, which is a member of the European Union (EU). The EU imposes "
                   "barriers to trade including data localization requirements that hinder cross-border trade and "
                   "extensive subsidies to the European aerospace industry.",
        "Spain": "The company does business in Spain, which is a member of the European Union (EU). The EU imposes "
                 "barriers to trade including data localization requirements that hinder cross-border trade and "
                 "extensive subsidies to the European aerospace industry.",
        "Slovakia": "The company does business in Slovakia, which is a member of the European Union (EU). "
                    "The EU imposes barriers to trade including data localization requirements that hinder "
                    "cross-border trade and extensive subsidies to the European aerospace industry.",
        "Sweden": "The company does business in Sweden, which is a member of the European Union (EU). The EU "
                  "imposes barriers to trade including data localization requirements that hinder cross-border "
                  "trade and extensive subsidies to the European aerospace industry.",
        "Slovenia": "The company does business in Slovenia, which is a member of the European Union (EU). The "
                    "EU imposes barriers to trade including data localization requirements that hinder cross-border "
                    "trade and extensive subsidies to the European aerospace industry.",
        "European Union": "The company does business in the European Union (EU). The European Union imposes "
                          "barriers to trade including data localization requirements that hinder cross-border trade "
                          "and extensive subsidies to the European aerospace industry.",
        "Ghana": "The company does business in Ghana. Ghana maintains barriers to trade including local content and "
                 "location participation requirements and investment restrictions in key sectors.",
        "Guatemala": "The company does business in Guatemala. Guatemala maintains barriers to trade including complex "
                     "and unclear laws and regulations and inconsistent judicial decisions.",
        "Honduras": "The company does business in Honduras. Honduras few barriers to trade in goods and services "
                    "and few restrictions on foreign capital flows and investment.",
        "Hong Kong": "The company does business in Hong Kong. Hong Kong maintains few barriers to trade in goods and "
                     "services and few restrictions on foreign capital flows and investment.",
        "India": "The company does business in India. India imposes barriers to trade including significant tariff and "
                 "nontariff barriers that impede imports of U.S. products into India. Further, India imposes data "
                 "localization requirements that hinder cross-border digital trade.",
        "Indonesia": "The company does business in Indonesia. Indonesia maintains barriers to trade including "
                     "overlapping import licensing requirements and prohibitions on foreign investment in key sectors.",
        "Israel": "The company does business in Israel. Israel maintains few barriers to trade in goods and "
                  "services and few restrictions on foreign capital flows and investment.",
        "Japan": "The company does business in Japan. Japan imposes barriers to trade including foreign direct "
                 "investment barriers and a lack of market access in certain sectors.",
        "Jordan": "The company does business in Jordan. Jordan imposes barriers to trade including special taxes on "
                  "various goods, overlapping import licensing requirements, and required localization of information "
                  "and technology firms.",
        "Kenya": "The company does business in Kenya. Kenya imposes barriers to trade including a complex import "
                 "licensing regime, data localization requirements, and foreign equity participation restrictions.",
        "Kuwait": "The company does business in Kuwait. Kuwait imposes limitations on foreign investment in key "
                  "sectors.",
        "Laos": "The company does business in Laos. Laos maintains few barriers to trade in goods and services and few "
                "restrictions on foreign capital flows and investment.",
        "Malaysia": "The company does business in Malaysia. Malaysia maintains few barriers to trade in goods and "
                    "services.",
        "Mexico": "The company does business in Mexico. Mexico maintains few barriers to trade in goods and "
                  "services and few restrictions on foreign capital flows and investment.",
        "Morocco": "The company does business in Morocco. Morocco maintains barriers to trade including "
                   "irregularities in government procedures.",
        "Myanmar (Burma)": "The company does business in Myanmar (Burma). Myanmar (Burma) imposes barriers to trade "
                           "including prohibiting investment in certain sectors, lack of protection of minority "
                           "investors, and pervasive smuggling.",
        "New Zealand": "The company does business in New Zealand. New Zealand maintains few barriers to trade in "
                       "goods and services and few restrictions on foreign capital flows and investment.",
        "Nicaragua": "The company does business in Nicaragua. Nicaragua imposes barriers to trade including weak "
                     "government institutions, deficiencies in rule of law, and extensive executive control.",
        "Nigeria": "The company does business in Nigeria. Nigeria imposes barriers to trade including arbitrary "
                   "customs enforcement and widespread smuggling.",
        "Norway": "The company does business in Norway. Norway maintains investment barriers to foreign companies, who "
                  "must seek prior government approval.",
        "Oman": "The company does business in Oman. Oman maintains few barriers to trade in goods and services and "
                "few restrictions on foreign capital flows and investment.",
        "Pakistan": "The company does business in Pakistan. Pakistan imposes barriers to digital trade including data "
                    "localization laws, in addition to periodical blocking to Internet-based services deemed "
                    "blasphemous or immoral by the federal government.",
        "Panama": "The company does business in Panama. Panama maintains few barriers to trade in goods and "
                  "services and few restrictions on foreign capital flows and investment.",
        "Paraguay": "The company does business in Paraguay. Paraguay maintains investment barriers to foreign "
                    "companies which requires companies to demonstrate 'just cause' to terminate, modify, or decide "
                    "not to renew contracts with Paraguayan distributors.",
        "Peru": "The company does business in Peru. Peru maintains few barriers to trade in goods and services and few "
                "restrictions on foreign capital flows and investment.",
        "Qatar": "The company does business in Qatar. Qatar maintains various barriers to trade including a required "
                 "import license for the importation of most products, limitations on foreign equity participation"
                 ", and the requirement of a license to provide Voice over Internet Protocol (VoIP) services, "
                 "granting such licenses only to companies intending to charter in Qatar.",
        "Russia": "The company does business in Russia. The United States and Russia currently maintain sanctions "
                  "against one another. Russia further maintains various barriers to trade including high tariffs, "
                  "import substitution policies, data localization laws, and favorable market conditions for "
                  "state-owned enterprises.",
        "Saudi Arabia": "The company does business in Saudi Arabia. Saudi Arabia currently prohibits foreign "
                        "investment in ten sectors, including oil exploration, drilling and security. The "
                        "country further maintains data localization laws.",
        "Singapore": "The company does business in Singapore. The United States Trade Representative (USTR) "
                     "does not find significant market-wide trade barriers for companies doing business in Singapore.",
        "South Africa": "The company does business in South Africa. South Africa maintains few barriers to trade "
                        "in goods and services and few restrictions on foreign capital flows and investment.",
        "South Korea": "The company does business in South Korea. South Korea imposes barriers to trade including data "
                       "localization requirements and alleged disproportionate enforcement of anticompetitive "
                       "laws against foreign entities.",
        "Switzerland": "The company does business in Switzerland. Switzerland maintains barriers to trade in "
                       "regards to digital trade and electronic commerce which limits to the cross-border transfer "
                       "of personal data of Swiss subjects.",
        "Taiwan": "The company does business in Taiwan. Taiwan maintains few barriers to trade in goods and "
                  "services and few restrictions on foreign capital flows and investment.",
        "Thailand": "The company does business in Thailand. Thailand maintains barriers to trade including high tariff "
                    "rates, price controls, as well as limitations on foreign equity participation.",
        "The Philippines": "The company does business in the Philippines. The Philippines maintains barriers to "
                           "digital trade which requires cloud computing providers to partner with a 60% "
                           "Philippine owned company in order to participate in a government contract.",
        "Tunisia": "The company does business in Tunisia. Tunisia maintains barriers to trade including high "
                   "tariff rates, barriers to digital trade, restrictions to foreign investors that requires "
                   "approval by the federal government, and monopolies for state-owned enterprises.",
        "Turkey": "The company does business in Turkey. Turkey imposes barriers to trade including import "
                  "restrictions, government procurement restrictions, data localization laws, imposed regulation "
                  "on the use of encryption on hardware and software systems, and various investment barriers.",
        "Ukraine": "The company does business in Ukraine. Ukraine maintains investment barriers including "
                   "strict export controls.",
        "United Arab Emirates": "The company does business in the United Arab Emirates (UAE). The UAE imposes "
                                "barriers to digital trade as well as an investment law that mandates a minimum of "
                                "51% UAE national ownership.",
        "Vietnam": "The company does business in Vietnam. Vietnam imposes barriers to trade including bans on "
                   "imports of certain goods, forced data localization, price controls, and investment barriers.",
        "Venezuela": "The company does business in Venezuela. Venezuela is considered to have little formal, "
                     "large-scale, private sector cross-border trade whether due to government restrictions, armed "
                     "conflict, or natural disaster.",
        "United Kingdom": "The company does business in the United Kingdom. The United Kingdom imposes barriers "
                          "to trade including data localization requirements that hinder cross-border trade and "
                          "subsidies to the aerospace industry."
    }

    cin_list = cin.split(', ')
    green_cout = []
    yellow_cout = []
    red_cout = []
    no_colour = []

    for country in cin_list:
        if country in green_db:
            green_cout.append(country)
        elif country in yellow_db:
            yellow_cout.append(country)
        elif country in red_db:
            red_cout.append(country)
        else:
            no_colour.append(country)

    list.sort(green_cout)
    list.sort(yellow_cout)
    list.sort(red_cout)

    green_no = len(green_cout)
    yellow_no = len(yellow_cout)
    red_no = len(red_cout)

    separator = ", "
    green = separator.join(green_cout)
    yellow = separator.join(yellow_cout)
    red = separator.join(red_cout)

    if green_no >= 3:
        print(f"The company operates in {green}. These countries maintain few barriers to trade in goods and "
              f"services as well as few restrictions on foreign capital flows and investment.")
    else:
        for country in green_cout:
            print(countries.get(country))
    if yellow_no >= 3:
        print(f"The company operates in {yellow}. These countries maintain moderate barriers to trade in goods "
              f"and services or moderate restrictions on foreign capital flows and investment.")
    else:
        for country in yellow_cout:
            print(countries.get(country))
    if red_no >= 3:
        print(f"The company operates in {red}. These countries maintain significant barriers to trade including "
              f"import bans on certain products, severe restrictions on foreign investment, or monopolies by "
              f"State-Owned Enterprises (SOE's).")
    else:
        for country in red_cout:
            print(countries.get(country))
    for country in no_colour:
        if country == "the United States":
            print("The company does not operate in a country currently listed as imposing significant barriers to "
                  "trade by the United States Trade Representative.")

    print(f"Green: {green_cout}")
    print(f"Yellow: {yellow_cout}")
    print(f"Red: {red_cout}")
    print(f"Unrecognized: {no_colour}")
class Inspector:

    def __init__(self):
        self.documents_dict = {
            "passport": [],
            "ID_card": [],
            "access_permit": [],
            "work_pass": [],
            "grant_of_asylum": [],
            "certificate_of_vaccination": [],
            "diplomatic_authorization": []
        }
        self.documents_names =["passport",
                               "ID card",
                               "access permit",
                               "work pass",
                               "grant of asylum",
                               "certificate of vaccination",
                               "diplommatic authorization"]

        self.vaccinations_dict = {}

        self.actual_bulletin = {
            "allowed_nations": [],
            "denied_nations": [],
            "required_documents": self.documents_dict,
            "required_vaccinations": self.vaccinations_dict,
            "new_criminal": ""
        }

    def receive_bulletin(self, bulletin):
        nations_List = ["Arstotzka",
                        "Antegria",
                        "Impor",
                        "Kolechia",
                        "Obristan",
                        "Republia",
                        "United Federation"]

        bulletin_lines_List = bulletin.split("\n")

        def update_allowed_and_denied_nations():

            def return_commaless_line(line):
                if "," in line:
                    line = line.split(" ")
                    for i in range(len(line)):
                        line[i] = line[i].replace(",", "")
                    return " ".join(line)
                for nation in nations_List:
                    if nation in line:
                        return line

            def return_line_containing_nations(list):
                for line in list:
                    for nation in nations_List:
                        if (nation in line and "Allow citizens of " in line) or (nation in line and "Deny citizens of " in line):
                            return line

            def are_multi_lines_w_nations_Boolean(list):
                lines_with_nations = 0
                for line in list:
                    for nation in nations_List:
                        if nation in line:
                            lines_with_nations +=1
                            break
                    continue
                if lines_with_nations > 1:
                    return True
                else:
                    return False

            def return_lines_w_nations_List(list):
                lines = []

                for line in list:
                    for nation in nations_List:
                        if (nation in line and "Allow citizens of " in line) or (nation in line and "Deny citizens of " in line):
                            lines.append(line)
                            break

                return lines

            def return_allowed_nations_from_line_List(line):
                allowed_nations = [word for word in line.split(" ") if word in nations_List]

                if "United Federation" in line and "Allow citizens of " in line:
                    allowed_nations.append("United Federation")

                return allowed_nations

            def return_denied_nations_from_line_List(line):
                denied_nations = [word for word in line.split(" ") if word in nations_List and "Deny citizens of " in line]

                if "United Federation" in line and "Deny citizens of " in line:
                    denied_nations.append("United Federation")

                return denied_nations

            def update_actual_bulletin():

                for n in new_allowed_nations_List:

                    if n not in self.actual_bulletin["allowed_nations"]:
                        self.actual_bulletin["allowed_nations"].append(n)

                for n in new_denied_nations_List:

                    if n in self.actual_bulletin["allowed_nations"]:
                        self.actual_bulletin["allowed_nations"].remove(n)

            new_allowed_nations_List = []
            new_denied_nations_List = []

            if are_multi_lines_w_nations_Boolean(bulletin_lines_List):

                multi_lines_w_nations_List = return_lines_w_nations_List(bulletin_lines_List)

                for i in range(len(multi_lines_w_nations_List)):
                    multi_lines_w_nations_List[i] = return_commaless_line(multi_lines_w_nations_List[i])

                single_nations_line_list = [multi_lines_w_nations_List[i] for i in range(len(multi_lines_w_nations_List))]

                for line in single_nations_line_list:
                    if "Allow citizens of " in line:
                        new_allowed_nations_List.extend(return_allowed_nations_from_line_List(line))
                    elif "Deny citizens of " in line:
                        new_denied_nations_List.extend(return_denied_nations_from_line_List(line))

                update_actual_bulletin()

            else:
                if return_lines_w_nations_List(bulletin_lines_List) != []:
                    single_nations_line = return_commaless_line(return_line_containing_nations(bulletin_lines_List))
                    if "Allow citizens of " in single_nations_line:
                        new_allowed_nations_List.extend(return_allowed_nations_from_line_List(single_nations_line))
                    elif "Deny citizens of " in single_nations_line:
                        new_denied_nations_List.extend(return_denied_nations_from_line_List(single_nations_line))
                    update_actual_bulletin()

        def update_required_documents():
            documents_List = \
                ["passport",
                 "ID card",
                 "access permit",
                 "work pass",
                 "grant of asylum",
                 "certificate of vaccination",
                 "diplomatic authorization" ]

            underlined_documents_List = \
                ["passport",
                 "ID_card",
                 "access_permit",
                 "work_pass",
                 "grant_of_asylum",
                 "certificate_of_vaccination",
                 "diplomatic_authorization" ]

            def update_documents_Dict():

                for line in bulletin_lines_List:

                    if "Workers require work pass" in line:
                        self.documents_dict["work_pass"].append("Yes")

                    if "Entrants require " in line:
                        for document in documents_List:
                            if "Entrants require " + document in line:
                                self.documents_dict[underlined_documents_List[documents_List.index(document)]] = nations_List
                                continue

                    if "Foreigners require " in line:
                        for document in documents_List:
                            if "Foreigners require " + document in line:
                                self.documents_dict[underlined_documents_List[documents_List.index(document)]] = ["Antegria",
                                                                                                                  "Impor",
                                                                                                                  "Kolechia",
                                                                                                                  "Obristan",
                                                                                                                  "Republia",
                                                                                                                  "United Federation"]

                    if "Citizens of " in line:
                        if "vaccination" not in line:
                            for nation in nations_List:
                                for document in documents_List:
                                    if "Citizens of " + nation + " require " + document in line:
                                        self.documents_dict[underlined_documents_List[documents_List.index(document)]].append(nation)

            update_documents_Dict()

        def update_required_vaccinations():

            vaccine_Dict = {}
            for i, line in enumerate(bulletin_lines_List):
                if "vaccination" in line:
                    line_List = line.split(" ")

                    def return_commaless_line(list):
                        return [s.replace (",","") for s in list]

                    line_List = return_commaless_line(line_List)

                    if "United" in line_List:   # Because "United Federation" has a space between
                        line_List.remove("United")
                        line_List.remove("Federation")
                        line_List.append("United Federation")

                    vaccine_name_List = [w for w in line_List if line_List.index(w) > line_List.index("require") and line_List.index(w) < line_List.index("vaccination")]
                    vaccine_name = " ".join(vaccine_name_List)
                    vaccine_Dict[i] = vaccine_name

                    def bulletin_add_remove_vaccinations():

                        if "Entrants" in line_List: # Entrants meaning all nations_List
                            if "no" in line_List:
                                self.vaccinations_dict.pop(vaccine_Dict[i]) # Remove all nations_List
                            else:
                                self.vaccinations_dict[vaccine_Dict[i]] = nations_List   # Add all nations_List

                        elif "Foreigners" in line_List:   # Foreigners meaning all nations_List except Arstotzka

                            if "no" in line_List:
                                self.vaccinations_dict[vaccine_Dict[i]] = [x for x in self.vaccinations_dict[vaccine_Dict[i]]   # Remove all nations_List except Arstotzka
                                                                           if x not in ["Antegria", "Impor", "Kolechia", "Obristan", "Republia", "United Federation"]]
                            else:
                                self.vaccinations_dict[vaccine_Dict[i]] = ["Antegria", "Impor", "Kolechia", # Add all nations_List except Arstotzka
                                                                           "Obristan", "Republia",
                                                                           "United Federation"]

                        elif "Citizens of " in line_List:   # Followed by specific nations_List

                            if "no" in line_List:
                                self.vaccinations_dict[vaccine_Dict[i]] = [nation for nation in self.vaccinations_dict[vaccine_Dict[i]] if nation not in line_List]
                            else:
                                self.vaccinations_dict[vaccine_Dict[i]] = [nation for nation in nations_List if nation in line_List]

                    bulletin_add_remove_vaccinations()

        def update_new_criminal():
            for line in bulletin_lines_List:
                if "Wanted by the State:" in line:
                    line_List = line.split(" ")
                    wanted = line_List[line_List.index("State:") + 1] + " " + line_List[line_List.index("State:") + 2]
                    self.actual_bulletin["new_criminal"] = wanted

        update_allowed_and_denied_nations()

        update_required_documents()

        update_required_vaccinations()

        update_new_criminal()

    def inspect(self, entrant):

        nations_List = ["Arstotzka", "Antegria", "Impor", "Kolechia", "Obristan", "Republia", "United Federation"]

        documents_List = \
            ["passport",
             "ID card",
             "access permit",
             "work pass",
             "grant of asylum",
             "certificate of vaccination",
             "diplomatic authorization"]

        underlined_documents_List = \
            ["passport",
             "ID_card",
             "access_permit",
             "work_pass",
             "grant_of_asylum",
             "certificate_of_vaccination",
             "diplomatic_authorization"]

        def returns_nation():
            for document in entrant.values():
                for nation in nations_List:
                    if nation in document:
                        return nation

        def check_nation():

            if returns_nation() == "Arstotzka":
                return

            if returns_nation() not in self.actual_bulletin["allowed_nations"]:
                return "Entry denied: citizen of banned nation."

        def check_missing_documents():

            if entrant == {}:   # Missing all documents
                return "Entry denied: missing required passport."

            documents_req_for_nation_List = [doc for doc in self.documents_dict if returns_nation() in self.documents_dict[doc]]
            vaccine_certificates_req_for_nation_List = [vac_doc for vac_doc in self.vaccinations_dict if returns_nation() in self.vaccinations_dict[vac_doc]]

            if documents_req_for_nation_List == []:
                for doc in self.documents_dict.keys():
                    if self.documents_dict[doc] == nations_List:
                        documents_req_for_nation_List.append(doc)

            for document in documents_req_for_nation_List:

                if document not in entrant.keys():

                    if document == "access_permit":

                        if ("grant_of_asylum" in entrant.keys()):
                            return

                        if ("diplomatic_authorization" in entrant.keys()):
                            if "Arstotzka" in entrant.get("diplomatic_authorization"):
                                return

                            else:
                                return "Entry denied: invalid diplomatic authorization."

                    return "Entry denied: missing required " + documents_List[underlined_documents_List.index(document)] + "."

            if len(vaccine_certificates_req_for_nation_List) > 0:
                if "certificate_of_vaccination" not in entrant.keys():
                    return "Entry denied: missing required certificate of vaccination."

            if self.documents_dict["work_pass"] != []:
                for i in range(len(entrant.values())):
                    if "WORK" in list(entrant.values())[i]:
                        if "work_pass" not in entrant.keys():
                            return "Entry denied: missing required work pass."

        def check_mismatching_information():

            def check_mismatching_ID():

                document_and_ID_Dict = {}

                documents_and_keys_List = [key for key in entrant.keys()]

                for i, value in enumerate(entrant.values()):
                    for line in value.split("\n"):
                        if "ID#:" in line:
                            ID = line.split(" ")
                            for x in ID:
                                if "ID#:" in x:
                                    ID.pop(ID.index(x))
                                    document_and_ID_Dict[documents_and_keys_List[i]] = ID

                expected_value = next(iter(document_and_ID_Dict.values()))

                all_IDs_equal = all(value == expected_value for value in document_and_ID_Dict.values())

                if not all_IDs_equal:
                    return "Detainment: ID number mismatch."

            if "Detainment:" in str(check_mismatching_ID()):
                return check_mismatching_ID()

            def check_mismatching_name():

                document_and_name_Dict = {}

                documents_and_keys_List = [key for key in entrant.keys()]

                for i, value in enumerate(entrant.values()):
                    for line in value.split("\n"):
                        if "NAME:" in line:
                            name_line = line.split(" ")
                            for x in name_line:
                                if "NAME:" in x:
                                    name_line.pop(name_line.index(x))
                                    document_and_name_Dict[documents_and_keys_List[i]] = name_line


                expected_value = next(iter(document_and_name_Dict.values()))

                all_names_equal = all(value == expected_value for value in document_and_name_Dict.values())

                if not all_names_equal:
                    return "Detainment: name mismatch."

            if "Detainment:" in str(check_mismatching_name()):
                return check_mismatching_name()

            def check_mismatching_nation():

                document_and_nation_Dict = {}

                documents_and_keys_List = [key for key in entrant.keys()]

                for i, value in enumerate(entrant.values()):
                    for line in value.split("\n"):
                        if "NATION:" in line:
                            nation_line = line.split(" ")
                            for x in nation_line:
                                if "NATION:" in x:
                                    nation_line.pop(nation_line.index(x))
                                    document_and_nation_Dict[documents_and_keys_List[i]] = nation_line

                try:

                    expected_value = next(iter(document_and_nation_Dict.values()))

                    all_nations_equal = all(value == expected_value for value in document_and_nation_Dict.values())

                    if not all_nations_equal:
                        return "Detainment: nationality mismatch."

                except StopIteration:
                    pass

            if "Detainment:" in str(check_mismatching_nation()):
                return check_mismatching_nation()

            def check_mismatching_DOB():    # DOB - Date of Birth

                document_and_dob_Dict = {}

                for i, value in enumerate(entrant.values()):

                    for line in value.split("\n"):
                        if "DOB:" in line:
                            DOB_line = line.split(" ")
                            for x in DOB_line:
                                if "DOB:" in x:
                                    DOB_line.pop(DOB_line.index(x))
                                    document_and_dob_Dict[list(entrant.keys())[i]] = DOB_line

                try:

                    expected_value = next(iter(document_and_dob_Dict.values()))

                except Exception:
                    pass

                all_dobs_equal = all(value == expected_value for value in document_and_dob_Dict.values())

                if not all_dobs_equal:
                    return "Detainment: date of birth mismatch."

            if "Detainment:" in str(check_mismatching_DOB()):
                return check_mismatching_DOB()

        def check_missing_vaccination():

            nation = returns_nation()

            vaccines_req_for_nation_Dict = [vac for vac in self.vaccinations_dict if nation in self.vaccinations_dict[vac]]

            for vac in vaccines_req_for_nation_Dict:
                for i in range(len(list(entrant.values()))):
                    if vac not in list(entrant.values())[i]:
                        continue
                    else:
                        return

                return "Entry denied: missing required vaccination."

        def check_documents_expiration_date():

            document_and_exp_date_Dict = {}

            document_and_key_List = [key for key in entrant.keys()]

            for i, value in enumerate(entrant.values()):
                for line in value.split("\n"):
                    if "EXP:" in line:

                        date = line.split(" ")

                        for x in date:
                            if "EXP:" in x:

                                date.pop(date.index(x))
                                date_list = date[0].split(".")
                                document_and_exp_date_Dict[document_and_key_List[i]] = date_list

            for i in range(len(document_and_key_List)):
                if (document_and_key_List[i] != "diplomatic_authorization" and document_and_key_List[i] != "ID_card") and document_and_key_List[i] != "certificate_of_vaccination":

                    if document_and_exp_date_Dict[document_and_key_List[i]][0] < "1982":
                        return "Entry denied: " + documents_List[underlined_documents_List.index(document_and_key_List[i])]+ " expired."

                    elif document_and_exp_date_Dict[document_and_key_List[i]][0] == "1982":
                        if document_and_exp_date_Dict[document_and_key_List[i]][1] < "11":
                            return "Entry denied: " + documents_List[underlined_documents_List.index(document_and_key_List[i])]+ " expired."

                        elif document_and_exp_date_Dict[document_and_key_List[i]][1] == "11":
                            if document_and_exp_date_Dict[document_and_key_List[i]][2] <= "22":
                                return "Entry denied: " + documents_List[underlined_documents_List.index(document_and_key_List[i])]+ " expired."

        def return_criminal_name():
            for value in entrant.values():
                for line in value.split("\n"):
                    if "NAME:" in line:
                        name = line.split(" ")
                        name.pop(0)
                        for n in range(len(name)):
                            if "," in name[n]:
                                name[n] = name[n].replace(",", "")
                        return name[1] + " " + name[0]

        if len(entrant.keys()) > 1:
            if "Detainment:" in str(check_mismatching_information()):
                return check_mismatching_information()

        if return_criminal_name() == self.actual_bulletin["new_criminal"]:
            return "Detainment: Entrant is a wanted criminal."

        if "Entry denied: " in str(check_missing_documents()):
            return check_missing_documents()

        if "Entry denied: " in str(check_documents_expiration_date()):
            return check_documents_expiration_date()

        if "Entry denied: " in str(check_missing_vaccination()):
            return check_missing_vaccination()

        if "Entry denied: " in str(check_nation()):
            return "Entry denied: citizen of banned nation."

        if returns_nation() == "Arstotzka":
            return "Glory to Arstotzka."
        else:
            return "Cause no trouble."

result = open('out.txt', 'w', encoding='UTF-8')

def generate_vehicle_xml(wol1, wol2, mid1, mid2, go, ban):
    main_in_out = {
        "wol1": {"in": "517488002#0", "out": "506009345#2"},
        "wol2": {"in": "26005519#0", "out": "-26005519#0"},
        "mid1": {"in": "-796700658#1", "out": "796700658#1"},
        "mid2": {"in": "512187678#0", "out": "-512187678#18"},
        "ban": {"in": "-37400617#3", "out": "37400617#3"},
        "go": {"in": "794688376#0", "out": "-794688376#0"}
    }

    connections = {
        "wol1": ["wol2", "mid1", "ban", "go"],
        "wol2": ["mid1", "mid2", "wol1", "ban"],
        "mid1": ["wol2", "mid2"],
        "mid2": ["mid1", "ban", "go"],
        "ban": ["wol1", "mid2"],
        "go": ["wol1", "wol2", "mid1", "mid2", "ban"]
    }

    def get_out_links(main):
        return main_in_out[main]["out"].split(", ")

    vehicle_types = ["wol1", "wol2", "mid1", "mid2", "go", "ban"]
    vehicle_amount = [wol1, wol2, mid1, mid2, go, ban]
    total_vehicles = wol1 + wol2 + mid1 + mid2 + go + ban

    id_count = 0
    depart_count = 0

    for i in range(total_vehicles):
        if len(vehicle_types) == 0:
            break
        idx = i % len(vehicle_types)
        v_type = vehicle_types[idx]
        veh_id = f"veh{id_count}"
        depart_time = f"{depart_count * 0.10:.2f}"
        from_link = main_in_out[v_type]["in"]
        to_links = get_out_links(v_type)

        for to_main in connections[v_type]:
            # 제한된 연결만 수행
            if to_main != v_type:
                to_link = main_in_out[to_main]["out"]
                xml_string = f'<trip id="{veh_id}" type="veh_passenger" depart="{depart_time}" departLane="best" from="{from_link}" to="{to_link}"/>'
                result.write(xml_string + '\n')
                id_count+=1
                depart_count+=1
                veh_id = f"veh{id_count}"
                depart_time = f"{depart_count * 0.10:.2f}"
                vehicle_amount[idx] -= 1
                if vehicle_amount[idx] == 0:
                    vehicle_types.remove(v_type)
                    vehicle_amount.remove(vehicle_amount[idx])
                    break

def proportional_distribution(total_amount, ratios):
    total_ratio = sum(ratios)
    distribution = [int(total_amount * ratio / total_ratio) for ratio in ratios]
    return distribution

total_amount = 1000
# ratios = [16.70, 16.53, 14.40, 24.60, 13.89, 13.88]
# ratios = [18.44, 15.00, 16.62, 27.59, 11.08, 11.26]
# ratios = [17.13, 16.67, 14.72, 25.46, 12.83, 13.18]
# ratios = [18.30, 15.75, 15.87, 28.22, 10.95, 10.90]
# ratios = [18.14, 15.08, 14.00, 25.38, 12.28, 15.11]

# ratios = [20.5, 13.2, 28.5, 17, 10.5, 10.3]
ratios = [18.5, 15.2, 17, 28.5, 10.5, 10.3]

car = proportional_distribution(total_amount, ratios)

generate_vehicle_xml(car[0], car[1], car[2], car[3], car[4], car[5])
result.close()

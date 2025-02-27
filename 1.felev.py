valasz=input("Mondj egy hálózati eszközt!:     (switch/router/hub/workstation)\n")
if valasz == "switch":
    print("Ha egy másik switch-hez szeretnéd kötni, akkor kereszt(fordított) kábelt kell használni.")
    print("Ha egy hub-ba szeretnéd kötni, akkor kereszt(fordított) kábelt kell használni.")
    print("Ha egy workstation-höz szeretnéd kötni akkor egyenes kábelt kell használni.")
    print("Ha egy router-be szeretnéd kötni, akkor egyesnes kábelt kell használni.")
if valasz == "router":
        print("Ha egy másik router-hez szeretnéd kötni, akkor kereszt(fordított) kábelt kell használni.")
        print("Ha egy workstation-höz szeretnéd kötni, akkor kereszt(fordított) kábelt kell használni.")
        print("Ha egy hub-hoz szeretnéd kötni, akkor egyenes kábelt kell használni.")
        print("Ha egy switch-hez szeretnéd kötni, akkor egyenes kábelt kell használni.")

if valasz == "hub":
        print("Ha egy másik hub-hoz szeretnéd kötni, akkor kereszt(fordított) kábelt kell használni.")
        print("Ha egy switch-hez szeretnéd kötni, akkor kereszt(fordított) kábelt kell használni.")
        print("Ha egy router-hez szeretnéd kötni, akkor egyenes kábelt kell használni.")
        print("Ha egy workstation szeretnéd kötni, akkor egyenes kábelt kell használni.")
if valasz == "workstation":
        print("Ha egy router-hez szeretnéd kötni, akkor kereszt(fordított) kábelt kell használni.")
        print("Ha egy workstation-höz szeretnéd kötni, akkor kereszt(fordított) kábelt kell használni.")
        print("Ha egy hub-hoz szeretnéd kötni, akkor egyesnes kábelt kell használni.")
        print("Ha egy switch-hez szeretnéd kötni, akkor egyesnes kábelt kell használni.")
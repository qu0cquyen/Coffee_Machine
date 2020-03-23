spin = input()
electric_charge = input()

particle_dict = {"Strange": {"Class": "Quark", "Spin": "1/2", "Electric charge": "-1/3"},
                 "Charm": {"Class": "Quark", "Spin": "1/2", "Electric charge": "2/3"},
                 "Electron": {"Class": "Lepton", "Spin": "1/2", "Electric charge": "-1"},
                 "Muon": {"Class": "Lepton", "Spin": "1/2", "Electric charge": "0"},
                 "Photon": {"Class": "Boson", "Spin": "1", "Electric charge": "0"},
                 "Higgs boson": {"Class": "Boson", "Spin": "0", "Electric charge": "0"}}

for key in particle_dict:
    if spin == particle_dict[key]["Spin"] and electric_charge == particle_dict[key]["Electric charge"]:
        print(key, particle_dict[key]["Class"])

from Comune import Provincia
from Comune import Comune
import json
import geojson

class GameStateHandler:

    def __init__(self, provincia):
        self.provincia = provincia
        self.state = 0
    def save_state(self, outcome):
        # open old geojson save file, load that and close old save file
        # FORZATO PERCHE' FACEVA SCHIFO perché ancora non fetcho le risorse (penso)
        # outcome = ""
        old_save_file = open("./resources/state_"+str(self.state)+".geojson", "r", encoding="utf-8")
        whole_data = json.load(old_save_file)
        whole_data["event_description"] = outcome
        data = whole_data["data"]
        old_save_file.close()
        self.old_outcome = outcome
        for i in range(0,len(data["features"])):
            # saving comune
            sav_com = self.provincia.getComuneByName(data["features"][i]["properties"]["comune"])
            # set owner
            owner = sav_com.owned_by if sav_com.owned_by is not None else sav_com
            data["features"][i]["properties"]["owner"] = owner.name
            # set color
            data["features"][i]["properties"]["color"] = owner.color
        
        whole_data["data"] = data
        # increment save index and save new file
        self.state+=1
        with open("./resources/state_"+str(self.state)+".geojson", "w", encoding="utf-8") as f:
            geojson.dump(whole_data, f)

    def load_state(self, state):
        #TODO: implement
        pass
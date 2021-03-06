import os, json, glob
from tqdm import tqdm
import random
from face_classification.classify_image import classify

F_JPG = sorted(glob.glob('../examples/imgs/*.jpg'))
#random.shuffle(F_JPG)

for f in tqdm(F_JPG):
    f_json = f.replace('/imgs/', '/info/').replace('.jpg', '.json')

    if not os.path.exists(f_json):
        print(f"Removing {f}")
        os.remove(f)
        continue
        
    with open(f_json) as FIN:
        try:
            js = json.loads(FIN.read())
        except json.decoder.JSONDecodeError:
            print(f"Problem with json, removing {f}")
            os.remove(f)            
            continue

    if 'emotion_faces' in js:
        continue

    js['emotion_faces'] = classify(f)

    jst = json.dumps(js, indent=2)
    with open(f_json, 'w') as FOUT:
        FOUT.write(jst)

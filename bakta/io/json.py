import json

import bakta.constants as bc

def write_json(genome, features, json_path):
    # clean feature attributes
    for feat in features:
        if(feat['type'] == bc.FEATURE_CDS or feat['type'] == bc.FEATURE_SORF):
            feat.pop('aa_digest')  # remove binary aa digest before JSON serialization
            
            # remove redundant IPS Dbxrefs
            ips = feat.get('ips', None)
            if(ips):
                ips.pop('db_xrefs')
            
            # remove redundant PSC Dbxrefs
            psc = feat.get('psc', None)
            if(psc):
                psc.pop('db_xrefs')
    
    # replace features type dict by sorted feature list
    genome['features'] = features

    with json_path.open('w') as fh:
        json.dump(genome, fh, indent=4)
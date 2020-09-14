from flask import Flask, render_template, url_for, jsonify
import json
import pandas as pd

#Load samples.json file into variable 'data'
with open('data/samples.json') as f:
    data = json.load(f)

#Create dataframes for metadata & samples which can easily filtered through with .loc
Metadata = pd.DataFrame(data['metadata'])
Samples = pd.DataFrame(data['samples'])

#Create dictionary which contains the list of names/ids under the key 'names'
Names = {'names':data['names']}

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

#Returns dictionary of metadata for specific sample id which can be called in app.js using d3.json
@app.route('/metadata/<sample>')
def metadata(sample):
    sample_metadata = Metadata.loc[Metadata['id'] == int(sample),:]
    return sample_metadata.to_dict('records')[0]

#Returns dictionary of sample data for specific sample id which can be called in app.js using d3.json
@app.route('/samples/<sample>')
def sample(sample):
    #Filter Samples dataframe to find row containing corresponding sample id specified in the url endpoint
    sample_data = Samples.loc[Samples['id'] == sample,:]

    #Create new dataframe which has each otu_id,otu_label, and sample_value indexed
    sample_otu_data = pd.DataFrame(data={'otu_ids':sample_data['otu_ids'].values,
        'otu_labels':sample_data['otu_labels'].values,'sample_values':sample_data['sample_values'].values})
        
    #Return sorted dict based on sample_values
    sorted_otu_data = sample_otu_data.sort_values('sample_values',ascending=False)
    return sorted_otu_data.to_dict('records')[0]
    
#Returns dictionary which contains list of names under key 'names' which can be called in app.js using d3.json
@app.route('/names')
def names():
    return Names

if __name__ == '__main__':
    app.run(debug=True)
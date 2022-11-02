#Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3

def detect_labels(photo, bucket):

    client=boto3.client('rekognition')

    response = client.detect_labels(Image={'S3Object':{'Bucket':bucket,'Name':photo}},
        MaxLabels=10)

    print('Detected cat labels for ' + photo) 
    print()
    found_cat = False
    for label in response['Labels']:
        if label['Name'] == 'Cat':
            found_cat = True
            for instance in label['Instances']:
                print ("  Bounding box")
                print ("    Top: " + str(instance['BoundingBox']['Top']))
                print ("    Left: " + str(instance['BoundingBox']['Left']))
                print ("    Width: " +  str(instance['BoundingBox']['Width']))
                print ("    Height: " +  str(instance['BoundingBox']['Height']))
                print ("  Confidence: " + str(instance['Confidence']))
                print()
            return found_cat, label['Instances']['Confidence']
    return found_cat, 0


def main():
    photos=['']
    bucket=''
    for photo in photos:
        found_cat, confidence = detect_labels(photo, bucket)
        if found_cat:
            print("Found cat with confidence: " + str(confidence))
        else:
            print("No cat found")

if __name__ == "__main__":
    main()




import React from 'react';
import { Image } from 'expo-image';
import {Picker} from '@react-native-picker/picker';
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, TextInput, View, Button } from 'react-native';

export default function App() {

  const [value, onChangeValue] = React.useState('---');
  const [inputValue, setInputValue] = React.useState('Input value here')
  const [inputCase, setInputCase] = React.useState("Select case");

  function convertValue(value){
    /*
    kinopya ko lang po yung nasa exercise 6
    i mean nireuse ko po yung codes ng exercise 6
    */
    if (inputCase== "1") {
    var degrees = Math.floor(value)
    var minutes = Math.floor((value-degrees)*60)
    var seconds = Math.round((value-degrees-(minutes/60))*3600)

    var output = degrees.toString().concat("-", minutes.toString(), "-", seconds.toString())
    setOutputValue(output)
  }
  else {
    var elements = value.split("-")
    var output = parseFloat(elements[0]) + parseFloat(elements[1])/60 + parseFloat(elements[2])/3600
    setOutputValue(output)
  }

  return (
    <View style={styles.box}>
        <View style={styles.TitleBox}>
          <Text style={styles.titleText}> Azimuth DMS to Bearing DMS CONVERTER </Text>
        </View>

        <View style={styles.OutputBox}>
          <Text style={styles.titleText}> DMS Output: </Text>
          <Text style={styles.titleText}> {value} </Text>
        </View>


        <View style={styles.InputBox}>
          <View style={styles.InputBoxa}>
            <Text> Input Case </Text>
            <Picker
              selectedValue = {inputCase}
              onValueChange = {(itemValue, itemIndex) =>
                setInputCase(itemValue)
              }> 
              <Picker.Item label = "Azimuth to Bearing" value ="1" />
              <Picker.Item label = "Bearing to Azimuth" value = "2" />
            </Picker>
          </View>

          <View style={styles.InputBoxb}>
            <TextInput
              style = {styles.input}
              onChangeText  = {setInputValue}
              value = {inputValue}
            />
            <Button
              title = "CONVERT"
              onPress = {() => convertValue(inputValue)}
            />
          </View>
        </View>


        <View style={styles.Picbox}>
          <Image
            style = {styles.image}
            source = "C:\Users\peter\OneDrive\Mga Dokumento\UP 1st Yr\ 2nd Sem\GE 120\GE120_Manlapig\GE120_1C_MANLAPIG\Sunrise photo.jpg"
            contentFit = 'cover'
            transition = {1000}
          />
        </View>
    </View>
  );
}

const styles = StyleSheet.create({
  box: {
    flex: 1,
    backgroundColor: 'red',
    alignItems: 'center',
    justifyContent: 'center'
  },
  TitleBox: {
    width: '100%',
    height: '15%',
    backgroundColor:'cyan',
    alignItems: 'center',
    justifyContent: 'center'
  },
  titleText: {
    fontsize: 20,
    fontWeight: '600'
  }, 

  InputBox: {
    width: '100%',
    height: '30%',
    backgroundColor:'purple',
    alignItems: 'center',
    justifyContent: 'center'
  },

  InputBoxa: {
    flexDirection: 'column',
    width: '100%',
    height: '45%',
  },

  InputBoxb: {
    flex: 1,
    width: '100%',
    height: '45%',
  },

  input: {
    height: '50%',
    width: '70%',
    fontSize: 24,
    color: 'white'
  },
  
  OutputBox: {
    width: '100%',
    height: '25%',
    backgroundColor:'green',
    alignItems: 'center',
    justifyContent: 'center'
  },

  Picbox: {
    width: '100%',
    height: '40%',
    backgroundColor:'white',
    alignItems: 'center',
    justifyContent: 'center'
  },

  image: {
    flex: 1,
    width: '100%',
    backgroundColor: '#0553',
  }
})
}
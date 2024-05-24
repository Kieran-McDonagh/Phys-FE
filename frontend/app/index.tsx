import React from 'react';
import {View, Text, StyleSheet} from 'react-native';
import LoginScreen from './screens/LoginScreen';

export default function Index () {
  return (
    <View style={styles.container}>
      <LoginScreen/>
    </View>
  );
};

const styles = StyleSheet.create({
  container : {
    flex:1,
    justifyContent:'center',
    alignItems:'center'
  }
})
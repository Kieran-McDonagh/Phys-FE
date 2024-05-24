import React, { useState } from "react";
import { View, TouchableOpacity, Text, StyleSheet } from "react-native";

const LoginScreen = () => {
  const [counter, setCounter] = useState(0);

  const increaseCount = () => {
    setCounter(counter + 1);
  };

  const resetCount = () => {
    setCounter(0);
  };

  return (
    <View style={styles.container}>
      <Text style={styles.counterText}>Counter: {counter}</Text>
      <TouchableOpacity onPress={increaseCount}>
        <View style={styles.button}>
          <Text style={styles.buttonText}>+1</Text>
        </View>
      </TouchableOpacity>
      <TouchableOpacity onPress={resetCount}>
        <View style={styles.button}>
          <Text style={styles.buttonText}>Reset</Text>
        </View>
      </TouchableOpacity>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
  },
  button: {
    padding: 10,
    backgroundColor: "blue",
    borderRadius: 5,
    marginTop: 10,
    width: 100,
  },
  buttonText: {
    color: "white",
    margin: "auto",
  },
  counterText: {
    fontSize: 18,
  },
});

export default LoginScreen;

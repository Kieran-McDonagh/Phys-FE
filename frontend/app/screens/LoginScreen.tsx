import React from "react";
import { View, TouchableOpacity, Text, Alert, StyleSheet } from "react-native";

const LoginScreen = () => {
  const handleClick = () => {
    Alert.alert("Button clicked");
  };

  return (
    <View style={styles.container}>
      <TouchableOpacity onPress={handleClick}>
        <View style={styles.button}>
          <Text style={styles.buttonText}>Click me</Text>
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
  },
  buttonText: {
    color: "white",
  },
});

export default LoginScreen;

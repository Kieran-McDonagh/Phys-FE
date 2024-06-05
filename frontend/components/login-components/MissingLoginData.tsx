import React from "react";
import { Text, View, StyleSheet } from "react-native";

interface MissingLoginDataProps {
  message: string;
}

const MissingLoginData: React.FC<MissingLoginDataProps> = ({ message }) => {
  return (
    <View style={styles.container}>
      <Text style={styles.message}>{message}</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    marginTop: 10,
    padding: 10,
    borderRadius: 5,
  },
  message: {
    color: "red",
    fontSize: 20,
  },
});

export default MissingLoginData;

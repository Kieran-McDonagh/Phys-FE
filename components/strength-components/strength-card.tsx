import React from "react";
import { Text } from "../Themed";
import { StyleSheet } from "react-native";

const StrengthCard = () => {
  return <Text style={styles.text}>strength</Text>;
};

export default StrengthCard;

const styles = StyleSheet.create({
  text: {
    color: "black",
  },
});

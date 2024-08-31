import React from "react";
import { StyleSheet, Text, TextInput, View } from "react-native";

interface Props {
  weight: string;
  setWeight: (weight: string) => void;
}

const WeightInput: React.FC<Props> = ({ weight, setWeight }) => {
  const handleChange = (newWeight: string) => {
    setWeight(newWeight);
  };

  return (
    <View style={styles.container}>
      <Text style={styles.text}>Kg: </Text>
      <TextInput
        style={styles.input}
        onChangeText={handleChange}
        value={weight}
        autoCapitalize="none"
        keyboardType="numeric"
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    display: "flex",
    flexDirection: "row",
    justifyContent: "center",
    alignContent: "center",
    alignItems: "center",
  },
  text: {
    fontSize: 16,
    color: "white",
  },
  input: {
    backgroundColor: "white",
    height: 40,
    width: 30,
    textAlign: "center",
    color: "black",
  },
});

export default WeightInput;

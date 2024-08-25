import React from "react";
import { StyleSheet, Text, TextInput, View } from "react-native";

interface Props {
  notes: string;
  setNotes: (type: string) => void;
}

const WorkoutNotes: React.FC<Props> = ({ notes, setNotes }) => {
  return (
    <View style={styles.container}>
      <Text style={styles.text}>Notes:</Text>
      <TextInput style={styles.input} onChangeText={setNotes} value={notes} autoCapitalize="none" />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    paddingVertical: 10,
    paddingHorizontal: 20,
    flexDirection: "row",
    gap: 10,
    justifyContent: "center",
    alignItems: "center",
    borderWidth: 1,
  },
  text: {
    fontSize: 16,
    color: "white",
    borderWidth: 1,
    width: "15%"
  },
  input: {
    backgroundColor: "white",
    height: 40,
    borderWidth: 1,
    padding: 10,
    width: "70%",
    textAlign: "center",
  },
});

export default WorkoutNotes;

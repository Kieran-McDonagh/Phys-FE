import { StyleSheet, TextInput, TouchableOpacity } from "react-native";
import { Text, View } from "@/components/Themed";
import { useState } from "react";
import TypeChoice from "@/components/workout-modal-components/TypeChoice";
import WorkoutTitle from "@/components/workout-modal-components/WorkoutTitle";
import WorkoutNotes from "@/components/workout-modal-components/WorkoutNotes";
import WorkoutBody from "@/components/workout-modal-components/WorkoutBody";

export default function WorkoutModalScreen() {
  const [selectedType, setSelectedType] = useState("individual");
  const [title, setTitle] = useState("");
  const [notes, setNotes] = useState("");
  const [body, setBody] = useState("");

  return (
    <>
      <View style={styles.container}>
        <Text style={styles.title}>Workout modal</Text>
        <TypeChoice setSelectedType={setSelectedType}></TypeChoice>
        <WorkoutTitle title={title} setTitle={setTitle} />
        <WorkoutBody body={body} setBody={setBody} />
        <WorkoutNotes notes={notes} setNotes={setNotes} />
      </View>
    </>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: "flex-start",
    justifyContent: "flex-start",
    marginTop: 20,
    borderWidth: 1,
    borderColor: "red",
  },
  title: {
    fontSize: 20,
    fontWeight: "bold",
    alignSelf: "center",
    margin: 20,
  },
  separator: {
    marginVertical: 30,
    height: 1,
    width: "80%",
  },
  input: {
    backgroundColor: "white",
    height: 40,
    margin: 12,
    borderWidth: 1,
    padding: 10,
    width: "80%",
    textAlign: "center",
  },
  signInText: {
    color: "orange",
    fontSize: 20,
    marginTop: 20,
  },
  registerText: {
    color: "blue",
    fontSize: 20,
    marginTop: 20,
  },
});

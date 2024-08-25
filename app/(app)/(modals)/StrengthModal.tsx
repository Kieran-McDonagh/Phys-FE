import { StyleSheet, TouchableOpacity } from "react-native";
import { Text, View } from "@/components/Themed";
import React, { useState } from "react";
import WorkoutNotes from "@/components/workout-modal-components/WorkoutNotes";
import useWorkoutStore from "@/store/workoutStore";
import useUserStore from "@/store/userStore";

export default function WorkoutModalScreen() {
  const { user } = useUserStore();
  const { postWorkout } = useWorkoutStore();
  const [selectedType, setSelectedType] = useState("individual");
  const [title, setTitle] = useState("");
  const [notes, setNotes] = useState("");
  const [bodyFields, setBodyFields] = useState([{ key: "", value: "" }]);
  const [postSuccess, setPostSuccess] = useState(false);
  const [postFailure, setPostFailure] = useState(false);

  const handlePostWorkout = async () => {
    const body = Object.fromEntries(bodyFields.map(({ key, value }) => [key, value]));
    const workoutData = {
      type: selectedType,
      title: title,
      notes: notes,
      body,
    };
    if (user) {
      const { access_token, token_type } = user;
      try {
        await postWorkout(workoutData, access_token, token_type);
        setPostSuccess(true);
        setPostFailure(false);
      } catch (error) {
        setPostFailure(true);
        setPostSuccess(false);
        console.error("Error posting workout data:", error);
      }
    }
  };

  const handleAddField = () => {
    setBodyFields([...bodyFields, { key: "", value: "" }]);
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Workout modal</Text>
      <TouchableOpacity onPress={handleAddField}>
        <Text>Add Field</Text>
      </TouchableOpacity>
      <WorkoutNotes notes={notes} setNotes={setNotes} />
      <TouchableOpacity onPress={handlePostWorkout}>
        <Text>Save</Text>
      </TouchableOpacity>
      {postSuccess ? <Text>Workout Saved!</Text> : null}
      {postFailure ? <Text>Failed to save workout</Text> : null}
    </View>
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
});

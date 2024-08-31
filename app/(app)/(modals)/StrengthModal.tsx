import { StyleSheet, TouchableOpacity } from "react-native";
import { Text, View } from "@/components/Themed";
import React, { useState } from "react";
import WorkoutNotes from "@/components/workout-modal-components/WorkoutNotes";
import useWorkoutStore from "@/store/workoutStore";
import useUserStore from "@/store/userStore";
import PullExercise from "@/components/strength-components/pull-exercise";
import PushExercise from "@/components/strength-components/push-exercise";
import LegExercise from "@/components/strength-components/leg-exercise";

export default function WorkoutModalScreen() {
  const { user } = useUserStore();
  const { postWorkout } = useWorkoutStore();
  const [notes, setNotes] = useState("");
  const [postSuccess, setPostSuccess] = useState(false);
  const [postFailure, setPostFailure] = useState(false);
  const [pullExercise, setPullExercise] = useState("");
  const [pullWeight, setPullWeight] = useState("");
  const [pullSets, setPullSets] = useState([0, 0, 0, 0, 0]);

  const handlePostWorkout = async () => {
    const convertedPullWeight = pullWeight ? `${pullWeight}Kg` : "";
    const workoutData = {
      type: "strength",
      notes: notes,
      body: {
        pull: {
          exercise: pullExercise,
          weight: convertedPullWeight,
          sets: pullSets,
        },
      },
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

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Workout modal</Text>
      <PullExercise
        pullExercise={pullExercise}
        setPullExercise={setPullExercise}
        pullWeight={pullWeight}
        setPullWeight={setPullWeight}
        pullSets={pullSets}
        setPullSets={setPullSets}
      />
      {/* <PushExercise setPushExercise={setPushExercise}/>
      <LegExercise setLegExercise={setLegExercise} /> */}
      <WorkoutNotes notes={notes} setNotes={setNotes} />
      <TouchableOpacity style={styles.saveButton} onPress={handlePostWorkout}>
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
  saveButton: {
    alignSelf: "center",
  },
});

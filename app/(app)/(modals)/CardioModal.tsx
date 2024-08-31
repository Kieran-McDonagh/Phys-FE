import { StyleSheet, TouchableOpacity } from "react-native";
import { Text, View } from "@/components/Themed";
import React, { useState } from "react";
import WorkoutNotes from "@/components/workout-modal-components/WorkoutNotes";
import useWorkoutStore from "@/store/workoutStore";
import useUserStore from "@/store/userStore";
import ExerciseSelection from "@/components/CardioComponents/ExerciseSelection";
import DistanceInput from "@/components/CardioComponents/DistanceInput";
import TimeInput from "@/components/CardioComponents/TimeInput";

export default function WorkoutModalScreen() {
  const { user } = useUserStore();
  const { postWorkout } = useWorkoutStore();

  const [notes, setNotes] = useState("");
  const [distance, setDistance] = useState<string>("");
  const [time, setTime] = useState<string[]>(["", "", ""]);
  const [cardioType, setCardioType] = useState<string>("");
  const [postSuccess, setPostSuccess] = useState(false);
  const [postFailure, setPostFailure] = useState(false);
  const handlePostWorkout = async () => {
    const convertDistance = (distanceString: string) => {
      return distanceString ? `${distanceString}km` : "";
    };

    const convertTime = (time: string[]) => {
      const hours = time[0] ? `${time[0]}h` : `0h`;
      const minutes = time[1] ? `${time[1]}m` : `0m`;
      const seconds = time[2] ? `${time[2]}s` : `0s`;
      return [hours, minutes, seconds];
    };

    const workoutData = {
      type: "cardio",
      notes: notes,
      body: {
        cardioType: cardioType,
        distance: convertDistance(distance),
        time: convertTime(time),
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
      <Text style={styles.title}>Cardio modal</Text>
      <ExerciseSelection setCardioType={setCardioType} />
      <DistanceInput distance={distance} setDistance={setDistance} />
      <TimeInput time={time} setTime={setTime} />
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
    borderWidth: 1,
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

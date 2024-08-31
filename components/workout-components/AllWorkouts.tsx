import React from "react";
import { ScrollView, StyleSheet, Dimensions, View } from "react-native";
import CardioCard from "../CardioComponents/cardio-card";
import StrengthCard from "../strength-components/strength-card";

type cardioWorkoutBody = {
  cardioType: string;
  distance: string;
  time: string[];
};

type exercise = {
  exercise: string;
  weight: string;
  sets: number[];
};

type strengthWorkoutBody = {
  pull: exercise;
  push: exercise;
  leg: exercise;
};

type workoutData = {
  id: string;
  user_id: string;
  date_created: string;
  type: "cardio" | "strength";
  body: cardioWorkoutBody | strengthWorkoutBody;
  notes: string;
};

interface Props {
  allWorkouts: workoutData[];
}

const AllWorkouts: React.FC<Props> = ({ allWorkouts }) => {
  return (
    <ScrollView contentContainerStyle={styles.container}>
      {allWorkouts.map((workout, index) => (
        <View key={index}>
          {workout.type === "cardio" ? (
            <CardioCard workout={workout as workoutData & { type: "cardio"; body: cardioWorkoutBody }} />
          ) : (
            <StrengthCard workout={workout as workoutData & { type: "strength"; body: strengthWorkoutBody }} />
          )}
        </View>
      ))}
    </ScrollView>
  );
};

const { width } = Dimensions.get("window");

const styles = StyleSheet.create({
  container: {
    display: "flex",
    flexDirection: "column",
    justifyContent: "center",
    alignContent: "center",
    width: width * 0.9,
  },
});

export default AllWorkouts;

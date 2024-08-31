import React, { FC } from "react";
import { Text, View } from "../Themed";
import { StyleSheet } from "react-native";
import WorkoutActionButtons from "../workout-components/workout-action-buttons";
import ExerciseSegment from "./strength-exercise-segment";

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
  type: "strength";
  body: strengthWorkoutBody;
  notes: string;
};

interface Props {
  workout: workoutData;
}

const StrengthCard: FC<Props> = ({ workout }) => {
  const dateObject = new Date(workout.date_created);
  const formattedDate = dateObject.toLocaleDateString();
  const formattedTime = dateObject.toLocaleTimeString();
  return (
    <View style={styles.cardItem}>
      <View style={styles.dateContainer}>
        <Text style={styles.dateTime}>{formattedDate}</Text>
        <Text style={styles.dateTime}>{formattedTime}</Text>
      </View>
      <View style={styles.actionButtons}>
        <WorkoutActionButtons id={workout.id} />
      </View>
      <View>
        {workout.body.pull.exercise ? <ExerciseSegment exercise={workout.body.pull} /> : null}
        {workout.body.push.exercise ? <ExerciseSegment exercise={workout.body.push} /> : null}
        {workout.body.leg.exercise ? <ExerciseSegment exercise={workout.body.leg} /> : null}
      </View>
      {workout.notes ? (
        <View style={styles.notesContainer}>
          <Text style={styles.notes}>{workout.notes}</Text>
        </View>
      ) : null}
    </View>
  );
};

export default StrengthCard;

const styles = StyleSheet.create({
  cardItem: {
    display: "flex",
    borderRadius: 20,
    marginBottom: 10,
    overflow: "hidden",
  },
  dateContainer: {
    backgroundColor: "lightblue",
    display: "flex",
    justifyContent: "space-around",
    flexDirection: "row",
    padding: 3,
  },
  dateTime: {
    color: "black",
    fontSize: 16,
  },
  actionButtons: {
    display: "flex",
    flexDirection: "row",
    backgroundColor: "pink",
    justifyContent: "flex-end",
    paddingRight: 10,
    paddingTop: 5,
  },
  notesContainer: {
    backgroundColor: "red",
  },
  notes: {
    alignSelf: "center",
    fontSize: 20,
    margin: 5,
    color: "black",
  },
});

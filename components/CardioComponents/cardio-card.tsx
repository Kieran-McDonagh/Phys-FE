import React, { FC } from "react";
import { Text, View } from "react-native";
import { StyleSheet } from "react-native";
import WorkoutActionButtons from "../workout-components/workout-action-buttons";

type cardioWorkoutBody = {
  cardioType: string;
  distance: string;
  time: string[];
};

type workoutData = {
  id: string;
  user_id: string;
  date_created: string;
  type: "cardio";
  body: cardioWorkoutBody;
  notes: string;
};

interface Props {
  workout: workoutData;
}

const CardioCard: FC<Props> = ({ workout }) => {
    const dateObject = new Date(workout.date_created);
    const formattedDate = dateObject.toLocaleDateString();
    const formattedTime = dateObject.toLocaleTimeString();
  return (
    <View style={styles.cardItem}>
        <View style={styles.dateContainer}>
        <Text>{formattedDate}</Text>
        <Text>{formattedTime}</Text>
        </View>
      <View style={styles.typeContainer}>
        <Text style={styles.exerciseType}>{workout.body.cardioType}</Text>
        <WorkoutActionButtons id={workout.id} />
      </View>
      <View style={styles.distanceContainer}>
        <Text style={styles.distanceContainerText}>{workout.body.distance}</Text>
        <Text style={styles.distanceContainerText}>
          {`${workout.body.time[0]} ${workout.body.time[1]} ${workout.body.time[2]}`}
        </Text>
      </View>
      {workout.notes ? (
        <View style={styles.notesContainer}>
          <Text style={styles.notes}>{workout.notes}</Text>
        </View>
      ) : null}
    </View>
  );
};

export default CardioCard;

const styles = StyleSheet.create({
  cardItem: {
    display: "flex",
    borderRadius: 20,
    marginBottom: 10,
    overflow: "hidden",
  },
  dateContainer: {
    backgroundColor: 'lightblue',
    display: 'flex',
    justifyContent: 'space-around',
    flexDirection: 'row',
    padding: 3
  },
  typeContainer: {
    display: "flex",
    flexDirection: "row",
    backgroundColor: "pink",
    alignContent: "center",
    alignItems: "center",
    justifyContent: "space-around",
  },
  exerciseType: {
    alignSelf: "flex-start",
    fontSize: 40,
    margin: 10,
  },
  actionButtons: {
    alignSelf: "flex-end",
  },
  distanceContainer: {
    display: "flex",
    flexDirection: "row",
    justifyContent: "space-evenly",
    backgroundColor: "green",
  },
  distanceContainerText: {
    fontSize: 25,
    color: "black",
    margin: 5,
  },
  notesContainer: {
    backgroundColor: "red",
  },
  notes: {
    alignSelf: "center",
    fontSize: 20,
    margin: 5,
  },
});

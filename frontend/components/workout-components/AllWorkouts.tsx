import { ScrollView, StyleSheet, Text, View } from "react-native";

interface Props {
  allWorkouts: any[];
}

const AllWorkouts: React.FC<Props> = ({ allWorkouts }) => {
  return (
    <ScrollView contentContainerStyle={styles.container}>
      {allWorkouts.map((workout, index) => (
        <View key={index} style={styles.item}>
          <Text>Title: {workout.title}</Text>
          <Text>Type: {workout.type}</Text>
          <Text>Notes: {workout.notes}</Text>
          <Text>User ID: {workout.user_id}</Text>
          <Text>Date Created: {workout.date_created}</Text>
          <Text>Body: {JSON.stringify(workout.body, null, 2)}</Text>
        </View>
      ))}
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: {
    paddingVertical: 10,
    paddingHorizontal: 20,
  },
  item: {
    paddingVertical: 10,
    paddingHorizontal: 10,
    borderBottomWidth: 1,
    borderBottomColor: "#ccc",
    marginBottom: 10,
    backgroundColor: "#f9f9f9",
    borderRadius: 5,
  },
  text: {
    fontSize: 16,
  },
});

export default AllWorkouts;

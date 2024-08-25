import React from "react";
import { StyleSheet, Text, TextInput, View } from "react-native";

interface Props {
    time: string[];
    setTime: (time: string[]) => void;
  }
  
  const TimeInput: React.FC<Props> = ({ time, setTime }) => {
    // Handle input changes for hours, minutes, and seconds
    const handleTimeChange = (value: string, index: number) => {
      const updatedTime = [...time];
      updatedTime[index] = value;
      setTime(updatedTime);
    };
  
    return (
      <View style={styles.container}>
        <Text style={styles.text}>Time:</Text>
        <TextInput
          style={styles.input}
          onChangeText={(value) => handleTimeChange(value, 0)}
          value={time[0]}
          autoCapitalize="none"
          placeholder="HH"
          placeholderTextColor="black"
          keyboardType="numeric"
          maxLength={2}
        />
        <TextInput
          style={styles.input}
          onChangeText={(value) => handleTimeChange(value, 1)}
          value={time[1]}
          autoCapitalize="none"
          placeholder="MM"
          placeholderTextColor="black"
          keyboardType="numeric"
          maxLength={2}
        />
        <TextInput
          style={styles.input}
          onChangeText={(value) => handleTimeChange(value, 2)}
          value={time[2]}
          autoCapitalize="none"
          placeholder="SS"
          placeholderTextColor="black"
          keyboardType="numeric"
          maxLength={2}
        />
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
    width: "15%",
  },
  input: {
    width: 40,
    height: 40,
    borderColor: "gray",
    borderWidth: 1,
    textAlign: "center",
    fontSize: 18,
    marginHorizontal: 5,
    backgroundColor: "white",
  },
  colon: {
    fontSize: 18,
    marginHorizontal: 2,
  },
});

export default TimeInput;

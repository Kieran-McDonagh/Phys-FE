import React, { FC } from "react";
import { Text, View } from "../Themed";
import { StyleSheet, TouchableOpacity } from "react-native";

interface Props {
  index: number;
  count: number;
  setCount: (index: number, count: number) => void;
}

const RepCounter: FC<Props> = ({ index, count, setCount }) => {
  const increaseCount = () => {
    setCount(index, count + 1);
  };

  return (
    <View>
      <TouchableOpacity style={styles.counter} onPress={increaseCount}>
        <Text style={styles.text}>{count}</Text>
      </TouchableOpacity>
    </View>
  );
};

const styles = StyleSheet.create({
  counter: {
    height: 30,
    width: 30,
    borderRadius: 15,
    backgroundColor: 'white',
    justifyContent: 'center',
    alignItems: 'center',
  },
  text: {
    color: 'black',
  },
});

export default RepCounter;

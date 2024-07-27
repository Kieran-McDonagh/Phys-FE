import React, { useState } from "react";
import { StyleSheet, TextInput, TouchableOpacity } from "react-native";
import { Text, View } from "@/components/Themed";
import { router } from "expo-router";
import MissingLoginData from "@/components/login-components/MissingLoginData";
import useUserStore from "@/store/userStore";

export default function RegisterScreen() {
  const { registerUser } = useUserStore();
  const [email, setEmail] = useState("");
  const [username, setUsername] = useState("");
  const [fullName, setFullName] = useState("");
  const [password, setPassword] = useState("");
  const [missingField, setMissingField] = useState<string | null>(null);

  const handleRegister = async () => {
    if (!email || !username || !fullName || !password) {
      setMissingField("Missing Field");
      return;
    }
    try {
      await registerUser(email, username, fullName, password);
    } catch (error) {
      console.error("Registration failed:", error);
    }
  };

  const handleBackToLogin = () => {
    setMissingField(null);
    router.push("/login");
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Register</Text>
      <View style={styles.separator} lightColor="#eee" darkColor="rgba(255,255,255,0.1)" />
      <TextInput
        style={styles.input}
        placeholder="Username"
        placeholderTextColor="black"
        onChangeText={setUsername}
        value={username}
        autoCapitalize="none"
      />
      <TextInput
        style={styles.input}
        placeholder="Email"
        placeholderTextColor="black"
        onChangeText={setEmail}
        value={email}
        autoCapitalize="none"
      />
      <TextInput
        style={styles.input}
        placeholder="Full name"
        placeholderTextColor="black"
        onChangeText={setFullName}
        value={fullName}
        autoCapitalize="none"
      />
      <TextInput
        style={styles.input}
        placeholder="Password"
        placeholderTextColor="black"
        onChangeText={setPassword}
        value={password}
        secureTextEntry={true}
        autoCapitalize="none"
      />
      <TouchableOpacity onPress={handleRegister}>
        <Text style={styles.registerText}>Register</Text>
      </TouchableOpacity>
      <TouchableOpacity onPress={handleBackToLogin}>
        <Text style={styles.backToLogin}>Back to login</Text>
      </TouchableOpacity>
      {missingField && <MissingLoginData message={missingField} />}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: "center",
    justifyContent: "center",
  },
  title: {
    fontSize: 20,
    fontWeight: "bold",
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
  registerText: {
    color: "pink",
    fontSize: 20,
    marginTop: 20,
  },
  backToLogin: {
    color: "orange",
    fontSize: 20,
    marginTop: 20,
  },
});

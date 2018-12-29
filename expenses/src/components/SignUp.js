import React, { Component } from 'react';
import { View, Text, TextInput, Button } from 'react-native';
import axios from 'axios';


class SignUp extends Component {
  constructor(props) {
    super(props);
    this.state = {
      first_name: '',
      last_name: '',
      username: '',
      password: '',
      email: '',
    }
    this.onFirstNameChange = this.onFirstNameChange.bind(this);
    this.onLastNameChange = this.onLastNameChange.bind(this);
    this.onUsernameChange = this.onUsernameChange.bind(this);
    this.onPasswordChange = this.onPasswordChange.bind(this);
    this.onEmailChange = this.onEmailChange.bind(this);
    this.handleSignUp = this.handleSignUp.bind(this);
  }

  onFirstNameChange(first_name) {
    this.setState({first_name})
  }

  onLastNameChange(last_name) {
    this.setState({last_name})
  }

  onEmailChange(email) {
    this.setState({email})
  }

  onUsernameChange(username) {
    this.setState({username})
  }

  onPasswordChange(password) {
    this.setState({password})
  }

  handleSignUp() {
    endpoint = '/auth/register/';
    payload = {
      username: this.state.username,
      password: this.state.password,
      first_name: this.state.first_name,
      last_name: this.state.last_name,
      email: this.state.email
    };

    axios
      .post(endpoint, payload)
      .then(response => {
        const { token, user } = response.data;

        // set the returned token as the default auth header
        axios.defaults.headers.common.Authorization = `Token ${token}`;

        this.props.navigation.navigate('LoginScreen');
      })
      .catch(error => console.log(error))
  }

  render() {
    return (
      <View>
        <TextInput
          placeholder="first name"
          onChangeText={this.onFirstNameChange}
        />
        <TextInput
          placeholder="last name"
          onChangeText={this.onLastNameChange}
        />
        <TextInput
          placeholder="email"
          onChangeText={this.onEmailChange}
        />
        <TextInput
          placeholder="username"
          onChangeText={this.onUsernameChange}
        />
        <TextInput
          placeholder="password"
          onChangeText={this.onPasswordChange}
          secureTextEntry={true}
        />
        <Button onPress={this.handleSignUp} title="OK" />
      </View>
    );
  }
}

export default SignUp;

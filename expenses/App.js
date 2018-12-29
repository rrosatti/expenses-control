import React, { Component } from 'react';
import { StyleSheet, Text, View } from 'react-native';
import Login from './src/components/Login';
import SignUp from './src/components/SignUp';
import Expenses from './src/components/Expenses';
import ExpenseDetail from './src/components/ExpenseDetail';
import NewExpense from './src/components/NewExpense';
import { createStackNavigator, createAppContainer } from 'react-navigation';


const AppNavigator = createStackNavigator(
  {
    LoginScreen: { screen: Login },
    SignUpScreen: { screen: SignUp },
    ExpensesScreen: { screen: Expenses },
    ExpenseDetailScreen: { screen: ExpenseDetail },
    NewExpenseScreen: { screen: NewExpense }
  },
  {
    initialRouteName: 'LoginScreen'
  }
);

const AppContainer = createAppContainer(AppNavigator);

export default class App extends React.Component {
  render() {
    return (
      <AppContainer />
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});

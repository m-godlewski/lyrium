import React from 'react';
import 'chart.js/auto';
import {Pie} from 'react-chartjs-2';

const state = {
	labels: ['Test', 'February', 'March',
			 'April', 'May'],
	datasets: [
	  {
		label: 'Rainfall',
		backgroundColor: [
			'#B21F00',
			'#C9DE00',
			'#2FDE00',
			'#00A6B4',
			'#6800B4'
		],
		hoverBackgroundColor: [
			'#501800',
			'#4B5000',
			'#175000',
			'#003350',
			'#35014F'
		],
		data: [65, 59, 80, 81, 56]
	  }
	]
  }

// Index page form
class MainPage extends React.Component {

	// Constructor
	constructor(props) {
		super(props);
		this.state = {artistName: ""};
		this.handleChange = this.handleChange.bind(this);
		this.handleSubmit = this.handleSubmit.bind(this);
	}

	// Method that handles changes in text field
	handleChange(event) {
		this.setState({artistName: event.target.value});
	}
	
	// Method that handles event after "Analyse" button was pressed
	handleSubmit(event) {
		event.preventDefault();
		fetch("/analyse?artist_name=" + this.state.artistName)
        	.then(response => response.json())
        	.then(data => this.setState({analysisResults: data.results}));
		this.setState({analysis: true});
	}

	// Method that renders form with one input text field and one submit button
	render() {
		if (this.state.analysis){
			console.log(this.state);
			return (
				<div>
					<h1>{this.state.artistName}</h1>

					<Pie
						data={this.state.analysisResults}
						options={{
							title:{
								display:true,
								text:"Most Common Words",
								fontSize: 20
							},
							legend:{
								display:true,
								position:'right'
							}
						}}
					/>

			  </div>
			);
		}
		else{
			return (
				<form onSubmit={this.handleSubmit}>
					<label>
						<input type="text" value={this.state.value} onChange={this.handleChange}/>
					</label>
					<input type="submit" value="Analyse" />
				</form>
			);
		}
	}
}

export default MainPage;

import React from 'react';


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
				<h1>{this.state.artistName}</h1>
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

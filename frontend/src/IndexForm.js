import React from 'react';


class IndexForm extends React.Component {
	constructor(props) {
		super(props);
		this.state = {value: ''};
		this.handleChange = this.handleChange.bind(this);
		this.handleSubmit = this.handleSubmit.bind(this);
	}

	handleChange(event) {
		this.setState({value: event.target.value});
	}

	handleSubmit(event) {
		event.preventDefault();
		const data = {
			artist_name: this.state
		}
		console.log(data);
		const response = 
		fetch("http://127.0.0.1:5000/analyse?artist_name=" + data.artist_name)
			.then(response => response.json());
		console.log(response);
	}

	render() {
		return (
			<form onSubmit={this.handleSubmit}>
				<label>
					<input type="text" value={this.state.value} onChange={this.handleChange} />
				</label>
				<input type="submit" value="Analyse" />
			</form>
		);
	}
}

export default IndexForm;

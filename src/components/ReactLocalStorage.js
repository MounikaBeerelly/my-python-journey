import React, { Component } from 'react';

class ReactLocalStorage extends Component {
    constructor(props) {
        super(props);
        this.onChangeName = this.onChangeName.bind(this);
        this.onChangeAddress = this.onChangeAddress.bind(this);
        this.onChangeEmail = this.onChangeEmail.bind(this);
        this.onSubmit = this.onSubmit.bind(this);

        this.state= {
            name: '',
            address: '',
            email: ''
        }
    }
    onChangeName(e) {
        this.setState ({
            name: e.target.value
        })
    }
    onChangeAddress(e) {
        this.setState ({
            address: e.target.value
        })
    }
    onChangeEmail(e) {
        this.setState ({
            email: e.target.value
        })
    }
    onSubmit(e) {
        e.preventDefault();
        localStorage.setItem('data', JSON.stringify(this.state));
    }

    componentDidMount() {
        this.documentData = JSON.parse(localStorage.getItem('data'));
        if(localStorage.getItem('data')) {
            this.setState( {
                name: this.documentData.name,
                address:this.documentData.address,
                email: this.documentData.email
            })
        } else {
            this.setState({
                name: '',
                address: '',
                email: ''
            })
        }
    }
    render() {
        return (
            <div className= "container">
                <form onSubmit = { this.onSubmit }>
                    <div className="form-group">
                        <label>Name: </label>
                        <input type = "text"
                               placeholder = "enter name"
                               className = "form-control"
                               value = { this.state.name }
                               onChange = { this.onChangeName }
                               required />
                    </div>
                    <div className="form-group">
                        <label>Address: </label>
                        <input type = "text"
                               placeholder = "enter address"
                               className = "form-control"
                               value = { this.state.address }
                               onChange = { this.onChangeAddress }
                               required />
                    </div>
                    
                    <div className="form-group">
                        <label>Email: </label>
                        <input type = "email"
                               placeholder = "enter email"
                               className = "form-control"
                               value = { this.state.email }
                               onChange = { this.onChangeEmail }
                               required />
                    </div>
                    <div className="form-group">
                        <input type = "submit"
                               value = "Register"
                               className = "btn-btn-primary" />
                    </div>
                    
                </form>
            </div>
        )
    }
}
export default ReactLocalStorage;
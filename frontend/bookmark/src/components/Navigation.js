
import React, { Component } from 'react';

class Navigation extends Component{
	render(){
		return(
			<div className="row">
				<div className="container-fluid">
					<nav className="navbar navbar-dark bg-dark">
						<h1 className="text-light">
							{this.props.titleNav}
						</h1>
						<p className="justify-content-end">Usuario</p>
					</nav>

				</div>
			</div>
			
			
		)
	}
}
export default Navigation;
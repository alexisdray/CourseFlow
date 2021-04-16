import * as React from "react";
import * as reactDom from "react-dom";
import {Provider, connect} from "react-redux";
import {ComponentJSON} from "./ComponentJSON.js";
import OutcomeView from "./OutcomeView.js";
import {OutcomeBarOutcomeView} from "./OutcomeView.js";
import {getOutcomeByID} from "./FindState.js";
import {WorkflowForMenu, renderMessageBox, closeMessageBox} from './MenuComponents.js'

//Basic component representing the outcome view
class OutcomeTopView extends ComponentJSON{
    
    constructor(props){
        super(props);
        this.objectType="outcome";
    }
    
    render(){
        let data = this.props.data;
        var selector = this;
        let share;
        if(!read_only)share = <div class="floatbardiv" onClick={renderMessageBox.bind(this,data,"share_menu",closeMessageBox)}><img src={iconpath+"add_person.svg"}/><div>Sharing</div></div>
        
        return(
            <div id="outcome-wrapper" class="workflow-wrapper">
                <div class = "workflow-container">
                    <div class="workflow-details">
                        <WorkflowForMenu workflow_data={data} selected={this.state.selected} selectAction={(evt)=>{this.props.renderer.selection_manager.changeSelection(evt,selector)}}/>
                        {reactDom.createPortal(
                        share,
                        $("#floatbar")[0]
                        )}
                        <OutcomeView objectID={data.id} renderer={this.props.renderer}/>
                    </div>
                </div>
                {this.addEditable(data)}
            </div>
        );
    }
    
}
const mapOutcomeStateToProps = (state,own_props)=>(
    getOutcomeByID(state,own_props.objectID)
)
export default connect(
    mapOutcomeStateToProps,
    null
)(OutcomeTopView)


class OutcomeBarUnconnected extends ComponentJSON{
    render(){
        let data = this.props.data;
        var outcomebaroutcomes = data.map((outcome)=>
            <OutcomeBarOutcomeView key={outcome.outcome} objectID={outcome.outcome}/>
        );
        
        
        return reactDom.createPortal(
            <div id="outcome-bar-workflow" class="right-panel-inner">
                <h4 class="drag-and-drop">Outcomes:</h4>
                <div class="outcome-bar-outcome-block">
                    {outcomebaroutcomes}
                </div>
            </div>
        ,$("#outcome-bar")[0]);
    }
}
const mapOutcomeBarStateToProps = state =>(
    {data:state.outcomeproject}
)
export const OutcomeBar = connect(
    mapOutcomeBarStateToProps,
    null
)(OutcomeBarUnconnected)
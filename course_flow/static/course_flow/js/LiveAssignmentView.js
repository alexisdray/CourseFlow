import * as React from "react";
import * as reactDom from "react-dom";
import {WorkflowTitle, AssignmentTitle, TitleText, ActionButton, DatePicker} from "./ComponentJSON";
import {WorkflowForMenu,renderMessageBox,closeMessageBox} from "./MenuComponents";
import {deleteSelfLive, setAssignmentCompletion, addUsersToAssignment, updateLiveProjectValue,createAssignment, getAssignmentData, getAssignmentDataStudent, setWorkflowVisibility, getWorkflowNodes} from "./PostFunctions";
import {StudentManagement} from "./StudentManagement";
import {WorkflowVisibility} from "./LiveProjectView";
import * as Constants from "./Constants";
import flatpickr from "flatpickr";

export class LiveAssignmentMenu extends React.Component{
    constructor(props){
        super(props);
        this.state={view_type:"edit",assignment_data:props.assignment_data};
    }
    
    render(){
        let data = this.state.assignment_data;
        let liveproject = this.props.live_project_data;
        console.log(data);

        let view_buttons = this.getViewButtons().map(
            (item)=>{
                let view_class = "hover-shade";
                if(item.type==this.state.view_type)view_class += " active";
                return <div id={"button_"+item.type} class={view_class} onClick = {this.changeView.bind(this,item.type)}>{item.name}</div>;
            }
        );

        return(
            <div class="project-menu">
                <div class="project-header">
                    {reactDom.createPortal(
                        <AssignmentTitle data={data}/>,
                        $("#workflowtitle")[0]
                    )}
                    {reactDom.createPortal(
                        <a id='live-project-return' href={update_path["liveproject"].replace(0,liveproject.pk)} class='floatbardiv'>
                            <img src={iconpath+"goback.svg"}/>
                            <div>{gettext("Classroom")}</div>
                        </a>,
                        $("#floatbar")[0]
                    )}
                    <AssignmentView renderer={this.props.renderer} data={data}/>
                    
                </div>

                <div class="workflow-view-select hide-print">
                    {view_buttons}
                </div>
                <div class = "workflow-container">
                    {this.getContent()}
                </div>
            </div>
        );
    }

    getViewButtons(){
        return [
            {type:"edit",name:gettext("Edit")},
            {type:"report",name:gettext("Report")},
        ];
    }
    

    changeView(view_type){
        this.setState({view_type:view_type});
    }
    
    componentDidMount(){
    }



    getContent(){
        switch(this.state.view_type){
            case "edit":
                return (<LiveAssignmentEdit updateAssignment={this.updateAssignment.bind(this)} view_type={this.state.view_type} renderer={this.props.renderer} data={this.props.assignment_data} live_project_data={this.props.live_project_data}/>);
            case "report":
                return (<LiveAssignmentReport view_type={this.state.view_type} renderer={this.props.renderer}  data={this.props.assignment_data}/>);
        }
    }

    updateFunction(new_state){
        this.setState(new_state);
    }

    updateAssignment(new_values){
        this.setState({assignment_data:{...this.state.assignment_data,...new_values}});
    }                 
}


class LiveAssignmentEdit extends React.Component{
    constructor(props){
        super(props);
        this.state={...this.props.data,has_changed:false,user_data:{assigned_users:[],other_users:[]}};
        this.changed_values={};
    }

    render(){
        let data=this.state;
        console.log(this.state);
        let changeField = this.changeField.bind(this);
        let assigned_users=this.state.user_data.assigned_users.map(user=>
            <option value={user.user.id}>{Constants.getUserDisplay(user.user)+" ("+user.role_type_display+")"}</option>
        );
        let other_users=this.state.user_data.other_users.map(user=>
            <option value={user.user.id}>{Constants.getUserDisplay(user.user)+" ("+user.role_type_display+")"}</option>
        );

        let linked_workflow;
        if(this.state.task.linked_workflow){
            console.log("linked wf");
            console.log(this.state);
            let visibility = "not_visible";
            if(this.state.linked_workflow_access)visibility="visible";
            let warning;
            if(!this.state.linked_workflow_access)warning=(<div class="warning">{gettext("Warning: the linked workflow is not visible to those in the classroom")}</div>);
            linked_workflow =
            [
                <h4>{gettext("Linked Workflow")}:</h4>,
                warning,
                <WorkflowVisibility workflow_data={this.state.task.linked_workflow_data} visibility={visibility} visibilityFunction={this.switchVisibility.bind(this)}/>
            ];
        }
        let parent_workflow;
        if(this.state.user_data.parent_workflow){
            let parent_visibility = "not_visible";
            if(this.state.workflow_access)parent_visibility="visible";
            let warning;
            if(!this.state.workflow_access)warning=(<div class="warning">{gettext("Warning: the workflow the task appears in is not visible to those in the classroom")}</div>);
            parent_workflow=[
                <h4>{gettext("Task Workflow")}:</h4>,
                warning,
                <WorkflowVisibility workflow_data={this.state.user_data.parent_workflow} visibility={parent_visibility} visibilityFunction={this.switchVisibility.bind(this)}/>,
            ];
        }
        return (
            <div class="workflow-details">
                <h3>{gettext("Configuration")}:</h3>
                <div>
                    <label>{gettext("End Date")}: </label><DatePicker id="end_date" default_value={data.end_date} onChange={this.changeField.bind(this,"end_date")}/>
                </div>
                <div>
                    <label>{gettext("Start Date")}: </label><DatePicker id="start_date" default_value={data.start_date} onChange={this.changeField.bind(this,"start_date")}/>
                </div>
                <div>
                    <label for="single-completion" title={gettext("Whether to mark the assignment as complete if any user has completed it.")}>{gettext("Single Completion")}</label><input id="single-completion" name="single-completion" type="checkbox" checked={data.single_completion} onChange={(evt)=>changeField("single_completion",evt.target.checked)}/>
                </div>
                <div>
                    <label for="self-reporting" title={gettext("Whether students can mark their own assignments as complete.")}>{gettext("Self Reporting")}</label><input id="self-reporting" name="self-reporting" type="checkbox" checked={data.self_reporting} onChange={(evt)=>changeField("self_reporting",evt.target.checked)}/>
                </div>
                <div>
                <button disabled={(!this.state.has_changed)} onClick={this.saveChanges.bind(this)}>{gettext("Save Changes")}</button>
                </div>
                <div>
                <button onClick={this.delete.bind(this)}>{gettext("Delete")}</button>
                </div>
                <h3>{gettext("Users")}:</h3>
                
                <div>
                    <div class="multi-select">
                        <h5>{gettext("Assigned Users")}</h5>
                        <select id="users_chosen" multiple>
                            {assigned_users}
                        </select>
                        <button id="remove-user" onClick={this.removeUser.bind(this)}> {gettext("Remove")} </button>
                    </div>
                    <div class="multi-select">
                        <h5>{gettext("Other Users")}</h5>
                        <select id="users_all" multiple>
                            {other_users}
                        </select>
                        <button id="add-user" onClick={this.addUser.bind(this)}> {gettext("Add")} </button>
                    </div>
                </div>
                <h3>{gettext("Workflows")}:</h3>
                {parent_workflow}
                {linked_workflow}
                
            </div>
        );
    }

    switchVisibility(pk,visibility){
        console.log("switching visibility");
        let parameter="workflow_access";
        if(this.state.task.linked_workflow==pk)parameter="linked_"+parameter;
        if(visibility=="visible"){
            setWorkflowVisibility(this.props.live_project_data.pk,pk,true);
            let new_state={};
            new_state[parameter]=true;
            this.props.updateAssignment(new_state);
            this.setState(new_state);
        }else{
            setWorkflowVisibility(this.props.live_project_data.pk,pk,false);
            let new_state={};
            new_state[parameter]=false;
            this.props.updateAssignment(new_state);
            this.setState(new_state);
        }

    }

    delete(){
        let data = this.state;
        if(window.confirm(gettext("Are you sure you want to delete this ")+gettext("assignment")+"?")){
            deleteSelfLive(data.id,"liveassignment",(response_data)=>{
                window.location = update_path.liveproject.replace("0",data.liveproject);

            });
        }
    }

    changeField(type,new_value){
        console.log(new_value);
        let new_state={has_changed:true};
        new_state[type]=new_value;
        this.changed_values[type]=new_value;
        this.setState(new_state);
    }


    saveChanges(){
        console.log(this.changed_values);
        updateLiveProjectValue(
            this.state.id,
            "liveassignment",
            this.changed_values,
        );
        console.log("updating");
        console.log(this.changed_values);
        this.props.updateAssignment(this.changed_values);
        this.changed_values={};
        this.setState({has_changed:false});
    }

    changeView(workflow_id){
        this.setState({selected_id:workflow_id})
    }

    addUser(evt){
        let selected = parseInt($("#users_all").val());
        if(!selected)return;
        console.log(selected);
        let user_data = {...this.state.user_data};
        user_data.assigned_users = user_data.assigned_users.slice();
        user_data.other_users = user_data.other_users.slice();
        user_data.assigned_users.push(
            user_data.other_users.splice(
                user_data.other_users.findIndex((element)=>element.user.id==selected),
                1
            )[0]
        );
        this.setState({user_data:user_data});
        addUsersToAssignment(this.state.id,[selected],true);
    }

    removeUser(evt){
        let selected = parseInt($("#users_chosen").val());
        if(!selected)return;
        console.log(selected);
        let user_data = {...this.state.user_data};
        user_data.assigned_users = user_data.assigned_users.slice();
        user_data.other_users = user_data.other_users.slice();
        user_data.other_users.push(
            user_data.assigned_users.splice(
                user_data.assigned_users.findIndex((element)=>element.user.id==selected),
                1
            )[0]
        );
        this.setState({user_data:user_data});
        addUsersToAssignment(this.state.id,[selected],false);
    }

    componentDidMount(){
        let component=this;
        console.log(component.props);
        getAssignmentData(component.props.data.id,component.props.view_type,(data)=>{
            console.log("got assignment data")
            component.setState({user_data:data.data_package});
        });
    }

}


export class AssignmentView extends React.Component{
    constructor(props){
        super(props);
        this.state={is_dropped:false}
        if(props.data.user_assignment)this.state.completed=props.data.user_assignment.completed;
    }

    render(){
        let data = this.props.data;
        let node_data = data.task;
        let data_override;
        if(node_data.represents_workflow) data_override = {...node_data,...node_data.linked_workflow_data};
        else data_override={...node_data};
        let lefticon;
        let righticon;
        if(node_data.context_classification>0)lefticon=(
            <img title={
                renderer.context_choices.find(
                    (obj)=>obj.type==node_data.context_classification
                ).name
            } src={iconpath+Constants.context_keys[data.context_classification]+".svg"}/>
        )
        if(node_data.task_classification>0)righticon=(
            <img title={
                renderer.task_choices.find(
                    (obj)=>obj.type==node_data.task_classification
                ).name
            }src={iconpath+Constants.task_keys[node_data.task_classification]+".svg"}/>
        )
        let style = {backgroundColor:Constants.getColumnColour(node_data)};
        let mouseover_actions = [];
        let css_class = "node assignment";
        if(this.state.is_dropped)css_class+=" dropped";

        let linkIcon;
        let linktext = gettext("Visit linked workflow");
        let clickfunc = this.visitWorkflow.bind(this,node_data.linked_workflow);
        if(node_data.linked_workflow_data){
            if(node_data.linked_workflow_data.deleted)linktext=gettext("<Deleted Workflow>")
            if(node_data.linked_workflow_data.deleted)clickfunc=null;
        }
        if(data.linked_workflow_access && node_data.linked_workflow)linkIcon=(
            <div class="hover-shade linked-workflow" onClick={clickfunc}>
                <img src={iconpath+"wflink.svg"}/>
                <div>{linktext}</div>
            </div>
        );
        let parentLinkIcon;
        let parentlinktext = gettext("Visit containing workflow");
        let parentclickfunc = this.visitWorkflow.bind(this,node_data.parent_workflow_id);
        if(data.workflow_access && data.parent_workflow_id)parentLinkIcon=(
            <div class="hover-shade linked-workflow" onClick={parentclickfunc}>
                <img src={iconpath+"wflink.svg"}/>
                <div>{parentlinktext}</div>
            </div>
        );
        let dropText = "";
        if(data_override.description&&data_override.description.replace(/(<p\>|<\/p>|<br>|\n| |[^a-zA-Z0-9])/g,'')!='')dropText="...";

        let dropIcon;
        if(this.state.is_dropped)dropIcon = "droptriangleup";
        else dropIcon = "droptriangledown";

        let completion_data;
        if(data.user_assignment){
            let disabled = true;
            console.log(this.props.renderer.user_role);
            if(this.props.renderer.user_role==Constants.role_keys.teacher || data.self_reporting)disabled=false;
            completion_data=(
                <div>
                    <label>{gettext("Completion")}: </label><input type="checkbox" disabled={disabled} checked={this.state.completed} onChange={this.changeCompletion.bind(this)}/>
                </div>
            )
        }
        console.log("making an assignmnet");
        console.log(this.props.renderer);

        return (
            <div style={style} class={css_class}>
                <div class="mouseover-actions">
                    {mouseover_actions}
                </div>
                <div class = "node-top-row">
                    <div class = "node-icon">
                        {lefticon}
                    </div>
                    <AssignmentTitle user_role={this.props.renderer.user_role} data={data}/>
                    <div class = "node-icon">
                        {righticon}
                    </div>
                </div>
                <div class="assignment-timing">
                    <div>
                        <div>
                            <label>{gettext("End Date")}: </label><DatePicker id="end_date" default_value={data.end_date} disabled={true}/>
                        </div>
                        <div>
                            <label>{gettext("Start Date")}: </label><DatePicker id="start_date" default_value={data.start_date} disabled={true}/>
                        </div>
                    </div>
                    <div>
                        {completion_data} 
                    </div>
                </div>
                {parentLinkIcon}
                {linkIcon}
                <div class = "node-details">
                    <TitleText text={data_override.description} defaultText={gettext("No description given")}/>
                </div>
                <div class = "node-drop-row hover-shade" onClick={this.toggleDrop.bind(this)}>
                    <div class = "node-drop-side node-drop-left">{dropText}</div>
                    <div class = "node-drop-middle"><img src={iconpath+dropIcon+".svg"}/></div>
                    <div class = "node-drop-side node-drop-right">
                        <div class="node-drop-time">{data_override.time_required && (data_override.time_required+" "+this.props.renderer.time_choices[data_override.time_units].name)}</div>
                    </div>
                </div> 
            </div>
        );
    }

    visitWorkflow(evt){
        let path=update_path["workflow"];
        evt.stopPropagation();
        if(this.props.data.task.linked_workflow){
            window.open(path.replace("0",this.props.data.task.linked_workflow));
        }
    }

    toggleDrop(){
        this.setState((state)=>{
            return {is_dropped:!state.is_dropped};
        });
    }

    changeCompletion(evt){
        let checked = evt.target.checked;
        this.setState({completed:checked});
        setAssignmentCompletion(this.props.data.user_assignment.id,checked);
    }

}


class LiveAssignmentReport extends React.Component{
    constructor(props){
        super(props);
        this.state={};
    }

    render(){
        console.log(this.state);
        if(!this.state.userassignments){
            return this.defaultRender();
        }

        let rows = this.state.userassignments.map(assignment=>
            <ReportRow userassignment={assignment} updateFunction={this.updateCompletion.bind(this)}/>
        );

        let total_completion = this.state.userassignments.reduce((accumulator,currentValue)=>
            accumulator+currentValue.completed,
            0
        );

        return (
            <div class="workflow-details">
                <h3>{gettext("Completion")}:</h3>
                <table>
                    {rows}
                    <tr>
                        <td>{gettext("Total")}:</td>
                        <td>{total_completion}/{this.state.userassignments.length}</td>
                    </tr>
                </table>
            </div>
        );
    }


    componentDidMount(){
        let component=this;
        console.log(component.props);
        getAssignmentData(component.props.data.id,component.props.view_type,(data)=>{
            console.log("got assignment data")
            component.setState({...data.data_package});
        });
    }

    defaultRender(){
        return (<renderers.WorkflowLoader/>);
    }

    updateCompletion(id,completed){
        let userassignments = this.state.userassignments.slice();
        let index = userassignments.findIndex((userassignment)=>userassignment.id==id);
        userassignmnets[index]={...userassignments[index],completed:completed};
        setAssignmentCompletion(id,completed);
    }

    
}

class ReportRow extends React.Component{
    render(){
        let user = this.props.userassignment.liveprojectuser;
        let userassignment=this.props.userassignment;
        let updateFuntion=this.props.updateFunction;
        return (
            <tr>
                <td>{Constants.getUserDisplay(user.user)+" ("+user.role_type_display+")"}</td>
                <td><input type="checkbox" checked={userassignment.completed} onChange={(evt)=>updateFunction(userassignment.id,evt.target.checked)}/></td>
            </tr>
        );
    }
}
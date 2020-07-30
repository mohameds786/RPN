import {Component, Input, OnInit} from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { NgModule } from '@angular/core';

@Component({
  selector: 'app-calc',
  templateUrl: './calc.component.html',
  styleUrls: ['./calc.component.scss']
})
export class CalcComponent implements OnInit {
  server_url = 'http://127.0.0.1:5000/rpn/stack';
  buttons;
  stackids;
  stackid;
  @Input() stack;
  @Input() value;
  options = ['Add the value', 'Delete the stack', 'Create a new stack'];
  constructor(private httpclient: HttpClient) {

  }

  ngOnInit(): void {
    this.getoperands();
    this.getstack();
  }

  refresh(): void {
    this.getstack();
    this.stackid = this.stackids[0];
    this.getastack(this.stackid);
  }

  async getstack(): Promise<any> {
    return this.httpclient.get('http://127.0.0.1:5000/rpn/stack').subscribe(data => {
      this.stackids =  data['stacks'];
    });
  }

  async getastack(stackid): Promise<any> {
    return this.httpclient.get('http://127.0.0.1:5000/rpn/stack'.concat('/', stackid)).subscribe(data => {
      console.log(data);
      this.stackid = stackid;
      this.stack = data['stack'];
      return data;
  });
  }

  async getoperands(): Promise<any> {
    return this.httpclient.get('http://127.0.0.1:5000/rpn/op').subscribe(data => {
      console.log(data);
      this.buttons = data['operations'];
    });
  }
  async operation(op): Promise<void> {
    console.log(op, this.stackid)
    var myurl = 'http://127.0.0.1:5000/rpn/op/'.concat(op, '/stack/', this.stackid);
    console.log(myurl);
    this.httpclient.request('POST', myurl, {body: {operation: op}}).subscribe();
    this.getastack(this.stackid);
  }

  async do_opt(opt): Promise<void> {
    if (opt === 'Add the value') {
      this.httpclient.request('POST', 'http://127.0.0.1:5000/rpn/stack/'.concat(this.stackid), {body: {value: this.value}}).subscribe();
      this.getastack(this.stackid);
    }
    if (opt === 'Delete the stack') {
      this.httpclient.request('DELETE', 'http://127.0.0.1:5000/rpn/stack/'.concat(this.stackid), {}).subscribe();
      this.refresh();
    }
    if (opt === 'Create a new stack') {
      this.httpclient.request('POST', 'http://127.0.0.1:5000/rpn/stack', {}).subscribe();
      this.refresh();
    }



  }

}
